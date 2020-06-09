import requests
import json

# response = json.loads(requests.get("https://makeup-api.herokuapp.com/api/v1/products.json").text)
# print(response)

with open('./assets/beauty_api.json', 'r') as f:
    response = json.loads(f.read())

vegan_makeup_list = []
vegan_dict= {'name':None, 'price':None, 'tag':None, 'description':None}


for i in range(len(response)):
    if 'Vegan' in response[i]['tag_list']:
        vegan_dict= {'name':None, 'price':None, 'tag':None, 'description':None}
        vegan_dict['name'] = response[i]['name']
        vegan_dict['price'] = response[i]['price']
        vegan_dict['tag'] = response[i]['tag_list']
        vegan_dict['description'] = response[i]['description']
        vegan_makeup_list.append(vegan_dict)

for i in vegan_makeup_list:
    print(i['name'])
    # print('\n\n')
    print('*************************************************')        

