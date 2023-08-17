import requests

FILE_NAME = "./images/"+"IMAGE_NAME_WITH_EXTENSION"
file = open(FILE_NAME,"rb").read()
res = requests.post("http://localhost:10000/api/recognize",files={"file":file}).json()
for user in res["predictions"]:
    print(user["userid"])
    
    
    
    
    