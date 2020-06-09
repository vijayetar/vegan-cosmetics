# import requests
import json

def beauty_api_call():
    # response = json.loads(requests.get("https://makeup-api.herokuapp.com/api/v1/products.json").text)

    with open('./assets/beauty_api.json', 'r') as f:
        response = json.loads(f.read())
    making_vegan_makeup_list(response)

def making_vegan_makeup_list(response):
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

    with open("./assets/vegan_cosmetics_data.txt", "w") as file: 
        for item in vegan_makeup_list:
            for key, value in item.items():
                string = f"{key}:  {value}\n"
                file.write("".join(string))

    
    return vegan_makeup_list   

    # for i in vegan_makeup_list:
    #     print(i['name'])
    #     # print('\n\n')
    #     print('*************************************************')     

if __name__ == "__main__":
    beauty_api_call()

