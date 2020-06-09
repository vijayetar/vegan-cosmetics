import requests
from bs4 import BeautifulSoup

test_url = "https://www.100percentpure.com/collections/fruit-dyed-makeup"

def get_contents_100percentpure():
  print('This is the website:  ', '100percent pure')
  # response = requests.get(test_url)
  # content = response.content
  # soup = BeautifulSoup(content, 'html.parser')
  # # print(soup.prettify())
  # cost = soup.findall('span', class_= 'original_price')
  # # <span class="original_price"><span class="money notranslate" data-gip-price-id="fyoFpoBTUfPfGOov" data-gip-original-value="22" data-gip-converted="false">$22.00</span></span>
  # # results = soup.find('div', id = "tab-description")
  # name = soup.findall('span', class_ = 'text-center m-t-sm flex j-c-center caption_text')
  # # <span class="text-center m-t-sm flex j-c-center caption_text">
  # #   <a href="/collections/fruit-dyed-makeup/products/fruit-pigmented-lip-gloss"><span class="same-height inline" same-height-id="productName" style="height: 16px;">Fruit Pigmented® Lip Gloss</span></a>
  # # </span>
  # print("*" * 100)
  # # print(results.get_text().strip())
  # # cost returns too many prices, isolate the one we want with an index value
  # for price in cost:
  #   print(price.get_text())
  # for item in name:
  #   print(item.get_text())
  # print("*" * 50)


if __name__ == "__main__":
  get_contents_100percentpure()