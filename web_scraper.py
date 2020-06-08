import requests
from bs4 import BeautifulSoup
# 100percentpure
URL = "https://www.100percentpure.com/collections/fruit-dyed-makeup/products/2nd-skin-corrector"
# MAC
URL1 = "https://www.maccosmetics.com/product/13854/310/products/makeup/lips/lipstick/matte-lipstick#!/shade/Chili"
# thrivecausemetics
URL2 = "https://thrivecausemetics.com/products/liquid-light-therapy-face-serum"
# billionvegans
URL3 = "https://billionvegans.com/product/andalou-naturals-luminous-eye-serum-brightening-0-6-fl-oz/"

def get_contents(URL):
  response = requests.get(URL)
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  cost = soup.findAll('span', id = 'ProductPrice' )
  results = soup.findAll('div', class_ = "m-b-sm text-base l-h ingredient-container")
  name = soup.findAll('h1', class_ = 'section_title_text')
  print("*" * 50)
  print(results[0].get_text().strip())
  print(cost[0].get_text().strip())
  print(name[0].get_text().strip())
  print("*" * 50)


def get_contents_1(URL1):
    response = requests.get(URL1)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    cost = soup.findAll('div', class_= 'product-price-v1 js-product-price-v1')
    results = soup.findAll('p', class_ = "js-product-full-iln-listing")
    name = soup.findAll('h1', class_ = 'product-full__name')
    print("*" * 50)
    print(results[0].get_text().strip())
    # cost returns too many prices, isolate the one we want with an index value
    print(cost[0].get_text().strip())
    print(name[0].get_text().strip())
    print("*" * 50)


def get_contents_2(URL2):
    response = requests.get(URL2)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    cost = soup.findAll('span', class_= 'product-main--price-item product-main--price-normal')
    # print(soup.prettify())
    results = soup.findAll('div', class_ = "ingredients--modal-content-body text--paragraph")
    name = soup.findAll('h1', class_ = 'product-main--title')
    print("*" * 50)
    print(results[0].get_text().strip())
    print(cost[0].get_text())
    print(name[0].get_text())
    print("*" * 50)


# <h1 class="product-main--title">Liquid Light Therapy All-in-One Face Serum™</h1>


def get_contents_3(URL3):
    response = requests.get(URL3)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    cost = soup.findAll('span', class_= 'woocommerce-Price-amount amount')
    results = soup.findAll('div', id = "tab-description")
    name = soup.findAll('h2', itemprop = 'name')
    print("*" * 50)
    print(results[0].get_text().strip())
    # cost returns too many prices, isolate the one we want with an index value
    print(cost[1].get_text())
    print(name[0].get_text())
    print("*" * 50)






# def get_citations_needed_count(URL):
#   citations = get_citations(URL)
#   return len(citations)
# def get_citation_list(URL):
#   citations = get_citations(URL)
#   cit_list = []
#   for cit in citations:
#     cit = cit.parent.text.strip()
#     cit_list.append(cit)
#   return_string = ""
#   for p in cit_list:
#     return_string += p + "\n" +"\n"
#   print(return_string)
#   return return_string
# def get_citation_headings(URL):
#     headings = []
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, "html.parser")
#     anchors = soup.find_all("a")
#     heading_tags = ['h1','h2','h3','h4','h5','h6']
#     for anchor in anchors:
#         text = anchor.get_text()
#         if "citation needed" in text:
#             elem = anchor.parent.parent.parent
#             for ps in elem.previous_siblings:
#                 if ps.name in heading_tags:
#                     headings.append(ps.text)
#                     break
#     return_string = ""
#     for p in headings:
#       return_string += p + "\n" +"\n"
#     print(return_string)
#     return return_string



if __name__ == "__main__":
    # get_contents(URL)
    # get_contents_1(URL1)
    # get_contents_2(URL2)
    get_contents_3(URL3)