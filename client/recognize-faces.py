import requests

FILE_NAME = ""
file = open(FILE_NAME,"rb").read()
res = requests.post("http://localhost:10000/api/recognize",files={"file":file})
for user in res["predictions"]:
    print(user["userid"])
    
    
    
    
    