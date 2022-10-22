# Image Webserver for SUAS AUVSI 2022
Groundstation webserver for receiving images, processing object detections and classifications, and submission to the interop system.

## Running
Python modules will most likely need to be installed which can be done by running the following command:
```
pip install -r requirements.txt
```
This presumes you have Python and pip installed.  
The server can be started by running `server.py`:
```
python server.py
```
## Submitting images
The server listens for HTTP POST requests at address `localhost/submit/`. It expects no arguments, and expects one file attached with key name `file`. Currently, it has only been tested using Postman but should work with in Python with the following code:
```python
import requests

url = "localhost/submit/"

payload={}
files=[
  ('file',('file.name',open('/path/to/image/being/submitted/file.name','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```
Or with cUrl from command line:
```
curl --location --request POST 'localhost/submit/' \
--form 'file=@"/path/to/image/being/submitted/file.name"'
```

### Submitting from other machines
Note that localhost will *only* work on the same machine. Two machines on the same local network (eg. WiFi) can communicate with each other using their local IP address. Running the server will print the local IP address to console - it should look something like `192.168.1.236`. An example URL would be `192.168.1.236/submit/`.

## User Interface
Once the server is running, navigate to [localhost](http://localhost) to view the user interface. It is hosted on port 80 (default HTTP port), so technically the port isn't ever needed. Sometimes detections don't load properly on initial page load; click an image on the right to refresh it.

## YOLO Large File Issue
YOLO weights are >100MB, which is the GitHub file size limit. The YOLO detections are currently commented out (line 40 in server.py), and a workaround should be available soon.