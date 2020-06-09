from textwrap import dedent
from vegan_cosmetics.beauty_api.beauty_api import beauty_api
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
  print('This is what you want', search_product)
  return search_product

if __name__ == "__main__":
    welcome_information()
    user_input()