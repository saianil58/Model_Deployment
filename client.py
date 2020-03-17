import requests
import json
url="http://localhost:8111/api"
data=json.dumps(
    {
        's1':3,
        's2':14.13,
        's3':4.1,
        's4':2.74,
        's5':24.5,
        's6':96,
        's7':2.05,
        's8':.76,
        's9':.56,
        's10':1.35,
        's11':.61,
        's12':1.6,
        's13':560
    })
r=requests.post(url,data)
print('the prediction is')
print(r.json())
