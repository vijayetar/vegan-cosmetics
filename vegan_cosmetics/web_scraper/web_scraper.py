import requests
import time
from bs4 import BeautifulSoup

hundred_percent_url = "https://www.100percentpure.com/collections/fruit-dyed-makeup"
thrive_causemetics_url = "https://thrivecausemetics.com/collections/all"

def get_contents_thrive_causemetics():
  with open ("./assets/thrive_cosmetics_saved.txt", "w") as file:
    file.write("")
  print('\n  Checking:  Thrive Causemetics Catalog')
  response = requests.get(thrive_causemetics_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  both = soup.find_all('div', class_= 'product-card-details')
  for item in both:
    deeper_url = f"https://thrivecausemetics.com{item.a['href']}"
    get_contents_thrive_causemetics_deeper(deeper_url)
    
def get_contents_thrive_causemetics_deeper(deeper_url):
  response = requests.get(deeper_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.find('span', class_ = 'product-main--price-item product-main--price-normal' )
  results = soup.find('div', class_ = 'ingredients--modal-content-body text--paragraph')
  name = soup.find('h1', class_ = 'product-main--title')
  with open ("./assets/thrive_cosmetics_saved.txt", "a+") as file:
    file.write(f"Name :   {name.get_text().strip()}  ")
    file.write(f"Cost :    {cost.get_text().strip()} \n")
    # file.write(results.get_text().strip())

def get_contents_100percentpure():
  with open ("./assets/hundred_percent_saved.txt", "w") as file:
    file.write("")
  print('\n  Checking:  100 Percent Pure Catalog')
  response = requests.get(hundred_percent_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  both = soup.find_all('div', class_= 'product-bottom')
  for item in both:
    deeper_url = f"https://www.100percentpure.com{item.span.a['href']}"
    get_contents_100percentpure_deeper(deeper_url)
  

def get_contents_100percentpure_deeper(deeper_url):
  response = requests.get(deeper_url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.find('span', class_ = 'section_title_text inline original_price' )
  results = soup.find('div', class_ = 'm-b-sm text-base l-h ingredient-container')
  name = soup.find('h1', class_ = 'section_title_text')
  with open ("./assets/hundred_percent_saved.txt", "a+") as file:
    file.write(f"Name :   {name.get_text().strip()}  ")
    file.write(f"Cost :    {cost.get_text().strip()} \n")
    # file.write(results.get_text().strip())

if __name__ == "__main__":
  pass
  # get_contents_100percentpure()
  # get_contents_thrive_causemetics()
