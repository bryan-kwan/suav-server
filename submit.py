# Sample test function for submitting images

import requests

url = "http://127.0.0.1//submit/"

payload={}
files=[
  ('file',('test.jpg',open('assets/suav.png','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)