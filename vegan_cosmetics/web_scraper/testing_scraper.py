import requests
from bs4 import BeautifulSoup

test_url = "https://www.100percentpure.com/collections/fruit-dyed-makeup"

def get_contents_100percentpure():
  print('This is the website:  ', '100percent pure')
  response = requests.get(test_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  both = soup.find_all('div', class_= 'product-bottom')
  print('This is the website:  ', '100 Percent Pure')
  for item in both:
    deeper_url = f"https://www.100percentpure.com{item.span.a['href']}"
    get_contents(deeper_url)
    print("\n")

def get_contents(deeper_url):
  response = requests.get(deeper_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.find('span', class_ = 'section_title_text inline original_price' )
  results = soup.find('div', class_ = 'm-b-sm text-base l-h ingredient-container')
  name = soup.find('h1', class_ = 'section_title_text')
  print("*" * 100)
  print(f"Name : {name.get_text().strip()}")
  print(f"Cost : {cost.get_text().strip()}")
  print(f"Ingredients:  {results.get_text().strip()}")
  print("*" * 100)

if __name__ == "__main__":
  get_contents_100percentpure()