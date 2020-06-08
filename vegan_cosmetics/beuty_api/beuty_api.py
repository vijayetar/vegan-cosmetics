import requests
import json
# parameters = {"tag_list": "Vegan"}

# Name, product, ingrediants 
# response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

# response_to_string = response.content.decode("utf-8")

# data = response.json()
# print(type(data))
# print(data)
# print(response.status_code)

# response = json.loads(requests.get("https://makeup-api.herokuapp.com/api/v1/products.json").text)
# print(response)

with open('./assets/beauty_api.json', 'r') as f:
    response = json.loads(f.read())

# print(response[0]['tag_list'])

# print(len(response[0]))

# print(response[0].items())
vegan_list = []

for i in range(len(response)):
    # print(response[i]['tag_list'])
    if 'Vegan' in response[i]['tag_list']:
        # for item in response[i]:
        #     if item == 'tag_list':
        # print(response[i]['name'])
        # print('\n')
        # print('************************************************ ')
        vegan_list.append(response[i])


print(vegan_list)
        

