import requests
import json

f = open('config.json')
data = json.load(f)
for upload in data['uploads']:
    files = {'file': open("./images/"+upload['file_name'], 'rb')}
    data = requests.post("http://localhost:10000/api/register",files=files,  data={"face_name": upload['file_name'], "userid": upload['face_name']}).json()
    print(data)




