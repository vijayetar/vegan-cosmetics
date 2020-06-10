import requests
from bs4 import BeautifulSoup

BV_URL = "https://billionvegans.com/product/andalou-naturals-luminous-eye-serum-brightening-0-6-fl-oz/"

#########################  Dictionary ################################
web_sites = [
    {
    'website': '100 Percent Pure',
    'url':"https://www.100percentpure.com/collections/fruit-dyed-makeup/products/2nd-skin-corrector", 
    'cost': ['span','section_title_text inline original_price'], 
    'description': ['div', "short-description caption_text m-b-sm"],
    'results': ['div', 'm-b-sm text-base l-h ingredient-container'],
    'name': ['h1','section_title_text']
    }, 
    {
    'website': 'Mac Cosmetics',
    'url':"https://www.maccosmetics.com/product/13854/310/products/makeup/lips/lipstick/matte-lipstick#!/shade/Chili", 
    'cost': ['div','product-price-v1 js-product-price-v1'], 
    'description': ['h2','product-full__short-desc'],
    'results': ['p', 'js-product-full-iln-listing'],
    'name': ['h1','product-full__name']
    }, 
    {
    'website': 'Thrive Causemetics',
    'url':"https://thrivecausemetics.com/products/liquid-light-therapy-face-serum", 
    'cost': ['span','product-main--price-item product-main--price-normal'], 'description':['div','accordion-body tab-body tab-body-1'],
    'results': ['div', 'ingredients--modal-content-body text--paragraph'],
    'name': ['h1','product-main--title']
    }
    ]

def get_contents(website, url, ele_cost, ele_cost_id, ele_desc, ele_desc_class, ele_results, ele_results_class, ele_name, ele_name_class):
  print('This is the website:  ', website)
  response = requests.get(url)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.find(ele_cost, class_ = ele_cost_id )
  results = soup.find(ele_results, class_ = ele_results_class)
  name = soup.find(ele_name, class_ = ele_name_class)
  print("*" * 100)
  print(website)
  print(name.get_text().strip())
  print(cost.get_text().strip())
  print(results.get_text().strip())
  print("*" * 100)

def get_contents_billion_vegans():
    print('This is the website:  ', 'Billion Vegans')
    response = requests.get(BV_URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    cost = soup.find('span', class_= 'woocommerce-Price-amount amount')
    results = soup.find('div', id = "tab-description")
    name = soup.find('h2', itemprop = 'name')
    print("*" * 100)
    print(results.get_text().strip())
    # cost returns too many prices, isolate the one we want with an index value
    print(cost.get_text())
    print(name.get_text())
    print("*" * 50)

def url_contents():
    for i in range(len(web_sites)):
        website = web_sites[i]['website']
        url = web_sites[i]['url']
        ele_cost = web_sites[i]['cost'][0]
        ele_cost_id = web_sites[i]['cost'][1]
        ele_desc = web_sites[i]['description'][0]
        ele_desc_class = web_sites[i]['description'][1]
        ele_results = web_sites[i]['results'][0]
        ele_results_class = web_sites[i]['results'][1]
        ele_name = web_sites[i]['name'][0]
        ele_name_class = web_sites[i]['name'][1]
        print(i)   
        get_contents(website, url, ele_cost, ele_cost_id, ele_desc, ele_desc_class, ele_results, ele_results_class, ele_name, ele_name_class)
    get_contents_billion_vegans()

if __name__ == "__main__":
    url_contents()
