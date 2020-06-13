import requests
import json
import re


def beauty_api_call():
    try:
        response = json.loads(requests.get("https://makeup-api.herokuapp.com/api/v1/products.json", timeout=10).text)

    except:
        with open('./assets/beauty_api.json', 'r') as f:
            response = json.loads(f.read())

    finally:
        vegan_makeup_list = making_vegan_makeup_list(response)
        print ('\n  Checking:  Beauty Catalog')
        return vegan_makeup_list



def making_vegan_makeup_list(response):
    vegan_makeup_list = []
    vegan_dict= {'name':None, 'price':None, 'tag':None, 'description':None}

    for i in range(len(response)):
        if 'Vegan' in response[i]['tag_list']:
            vegan_dict= {'name':None, 'price':None, 'tag':None, 'description':None}
            vegan_dict['name'] = response[i]['name']
            if re.search('[$]', response[i]['price']) or response[i]['price'] == '0.0':
                vegan_dict['price'] = f"{response[i]['price']}"
            elif response[i]['price']!='0.00':
                vegan_dict['price'] = f"${response[i]['price']}"
            vegan_dict['tag'] = response[i]['tag_list']
            vegan_dict['description'] = response[i]['description']
            vegan_makeup_list.append(vegan_dict)

    with open("./assets/vegan_cosmetics_data.txt", "w") as file: 
        for item in vegan_makeup_list:
            for key, value in item.items():
                string = f"{key}:  {value}\n"
                file.write("".join(string))

    return vegan_makeup_list       

if __name__ == "__main__":
    beauty_api_call()

