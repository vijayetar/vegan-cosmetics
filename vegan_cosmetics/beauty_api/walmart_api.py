import requests
import json

res = json.loads(requests.get("http://api.walmartlabs.com/v1/paginated/items?apiKey=jvjs99s69dgam83bmd4qdjbe&category=976760_2915579_5819635").text)
res = json.dumps(res, indent = 2)
print("this is from walmart", res)