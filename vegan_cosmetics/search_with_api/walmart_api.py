import requests
import json

api_key = "jvjs99s69dgam83bmd4qdjbe"

# this gives us the categeories to find the cosmetics in another api call

walmart_url = "http://api.walmartlabs.com/v1/taxonomy?apiKey=jvjs99s69dgam83bmd4qdjbe"

categories = json.loads(requests.get(walmart_url).text)
categories = json.dumps(categories, indent=2)

print(len(categories))

#works#1085666_7599906
#works#1085666_1007039
# "shortDescription" - vegan
res = json.loads(requests.get("http://api.walmartlabs.com/v1/paginated/items?apiKey=jvjs99s69dgam83bmd4qdjbe&category=976760_2915579_5819635").text)

res = json.dumps(res, indent = 2)
print("this is from walmart", res)