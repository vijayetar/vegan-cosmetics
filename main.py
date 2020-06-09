from textwrap import dedent
import re
from vegan_cosmetics.search_with_api.beauty_api import beauty_api_call
from vegan_cosmetics.search_with_regex.search_with_regex import search_with_regex
#User information
#User input
#Search API : match input with key values by name
#Search web page
##select item or all search is saved
#save to text file

def welcome_information():
  print(dedent('''
  *****************************************

  Welcome to our Vegan Cosmetic Site!!!

  *****************************************

  Press (q) to quit at any time
  '''))

def user_input():
  order_now = input(dedent(
  '''
  Would you like to order anything from our store (y/n)?
  '''))
  if order_now == 'y':
    search_product()
  elif order_now=='n' or order_now=='q':
    print("Thank you! Please come again. ")
  else:
    print("Please re-enter with y or n")
    user_input()

def search_product():
  search_product = input(dedent(
    '''
    What would you like to order?
    '''
  ))
  search_product = search_product.lower()
  find_search_product(search_product)


def find_search_product(search_product):
    regex_dict = {'mascara':'\b(\w*.ascara\w*)\b', 'foundation': '\b(\w*.oundation\w*)\b', 'eye shadow': '\b(\w*.hadow\w*)\b', 'lip products': '\b(\w*.ip\w*)\b', 'bronzer': '\b(\w*.onzer\w*)\b', 'liner': '\b(\w*.iner)\b', 'pencil' : '\b(\w*.encil)\b', 'blush' : '\b(\w*.lush)\b', 'cream' : '\b(\w*.ream\w*)\b', 'moisturizer': '\b(\w*.oistu\w*)\b', 'nail': '\b(\w*.ail\w*)\b', 'primer': '\b(\w*.rimer\w*)\b', 'powder': '\b(\w*.owder\w*)\b'}
    pattern = str(regex_dict[search_product])
    
    vegan_makeup_list = beauty_api_call()
    for item in vegan_makeup_list:
      print(item['name'])
# #     #check item['name'] to search_product
#         products = re.search(pattern,item['name'])
#         print(products)










if __name__ == "__main__":
    welcome_information()
    user_input()