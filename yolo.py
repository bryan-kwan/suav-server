import time
import cv2
import numpy as np
import glob
import json

#----------------------
# YOLO Detections File
#----------------------

CONFIDENCE_THRESHOLD = 0.3 # minimum probablity to filter weak detections
NMS_THRESHOLD = 0.1 # threshold for maxima supression

weights = glob.glob("yolo/yolov4-custom.weights")[0]
labels = glob.glob("yolo/custom.txt")[0]
cfg = glob.glob("yolo/yolov4-custom.cfg")[0]

lbls = list()
with open(labels, "r") as f:
	lbls = [c.strip() for c in f.readlines()]

net = cv2.dnn.readNetFromDarknet(cfg, weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
layer = net.getLayerNames()
layer = [layer[i - 1] for i in net.getUnconnectedOutLayers()]

def image_detections(imgpath):
	print('Detection for image', imgpath)
	image = cv2.imread("images/" + imgpath)
	(H, W) = image.shape[:2]

	blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), swapRB=True, crop=False)
	net.setInput(blob)
	start_time = time.time()
	layer_outs = net.forward(layer)
	end_time = time.time()

	boxes = list()
	confidences = list()
	class_ids = list()

	for output in layer_outs:
		for detection in output:
			scores = detection[5:]
			class_id = np.argmax(scores)
			confidence = scores[class_id]

			if confidence > CONFIDENCE_THRESHOLD:
				box = detection[0:4] * np.array([W, H, W, H])
				(center_x, center_y, width, height) = box.astype("int")

				x = int(center_x - (width / 2))
				y = int(center_y - (height / 2))

				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				class_ids.append(class_id)

	idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
	f = open("images\\" + imgpath + ".json", "w")
	result = {
		"inf time": "{:.2f}".format(end_time - start_time),
		"detections": []
		}
	if len(idxs) > 0:
		for i in idxs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			box = {
				"object": lbls[class_ids[i]],
				"confidence": "{:.4f}".format(confidences[i]),
				"x": x,
				"y": y,
				"width": w,
				"height": h
			}
			result["detections"].append(box)
	f.write(json.dumps(result))
	f.close()