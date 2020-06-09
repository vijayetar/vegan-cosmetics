import requests
import time
from bs4 import BeautifulSoup

# test_url = "https://www.100percentpure.com/collections/fruit-dyed-makeup"

# Jesse *****************************************************************************************
test_url2 = "https://thrivecausemetics.com/collections/all"

def get_contents_thrive_causemetics():
  print('This is the website:  ', 'Thrive Causemetics')
  response = requests.get(test_url2)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  both = soup.find_all('div', class_= 'product-card-details')
  # print(both.get_text().strip())
  # print(both.a['href'])
  for item in both:
    # print(item.a['href'])
    deeper_url = f"https://thrivecausemetics.com{item.a['href']}"
    # time.sleep(10)
    get_contents_thrive_causemetics_deeper(deeper_url)
    
    # print(both)
    print("\n")

def get_contents_thrive_causemetics_deeper(deeper_url):
  # try:
  # breakpoint()
  response = requests.get(deeper_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.find('span', class_ = 'product-main--price-item product-main--price-normal' )
  results = soup.find('div', class_ = 'ingredients--modal-content-body text--paragraph')
  name = soup.find('h1', class_ = 'product-main--title')
  print("*" * 100)
  print(f"Name : {name.get_text().strip()}")
  print(f"Cost : {cost.get_text().strip()}")
  print(f"Ingredients:  {results.get_text().strip()}")
  print("*" * 100)
  # except ValueError('Website could not be reached')

# Jesse ****************************************************************************************

# def get_contents_100percentpure():
#   print('This is the website:  ', '100percent pure')
#   response = requests.get(test_url)
#   content = response.content
#   soup = BeautifulSoup(content, 'html.parser')
#   # print(soup.prettify())
#   both = soup.find_all('div', class_= 'product-bottom')
#   for item in both:
#     deeper_url = f"https://www.100percentpure.com{item.span.a['href']}"
#     get_contents(deeper_url)
#     print("\n")

# def get_contents(deeper_url):
#   response = requests.get(deeper_url)
#   content = response.content
#   soup = BeautifulSoup(content, 'html.parser')
#   # print(soup.prettify())
#   cost = soup.find('span', class_ = 'section_title_text inline original_price' )
#   results = soup.find('div', class_ = 'm-b-sm text-base l-h ingredient-container')
#   name = soup.find('h1', class_ = 'section_title_text')
#   print("*" * 100)
#   print(f"Name : {name.get_text().strip()}")
#   print(f"Cost : {cost.get_text().strip()}")
#   print(f"Ingredients:  {results.get_text().strip()}")
#   print("*" * 100)

if __name__ == "__main__":
  # get_contents_100percentpure()
  get_contents_thrive_causemetics()
  # get_contents_thrive_causemetics_deeper(deeper_url)