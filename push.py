server = "https://api.pushbullet.com/v2/pushes"
import requests
import json

def push_notification(title,msg,email):

    headers = {"Content-Type" : "application/json",
               "Access-Token" : "o.YXx1TOEID780wLclEcLs2ktAAmfZqCaO"}

    data = {"type" : "note",
            "title" : title,
            "body" : msg,
            "email" : email}
    json_data = json.dumps(data)

    res = requests.post(url=server, data=json_data, headers=headers)
    print(res.content)