from textwrap import dedent
import re
from vegan_cosmetics.search_with_api.beauty_api import beauty_api_call
import sys

def welcome_information():
  """
  Initial function.  Greets the user and then calls the user_input function which ultimately allows the user to say whether or not they want to order from the store.
  """
  print(dedent('''
  *****************************************

  Welcome to our Vegan Cosmetic Site!!!

  *****************************************

  Press (q) to quit at any time
  '''))
  user_input()

def reset_user_fav_list():
  """
  Function that resets the users favorite list
  """
  user_fav_list = []
  return user_fav_list

def user_input(user_fav_list = []):
  """
  Function takes in user input whether or not they want to order anything from our store, if they do, then it brings in the search products function and allows them to order.  If they dont, the program will quit. Also Covers the edge case, if they enter the wrong input, it will ask them the question again.  
  """
  order_now = input(dedent(
  '''
  Would you like to order anything from our store (y/n)?
  '''))

  if order_now == 'y':
    search_product(user_fav_list)

  # elif order_now=='n' or order_now=='q':
  #   print("Thank you! Please come again. ")

  elif order_now == 'n':
    grab_saved_product()

  elif order_now == 'q':
    print("Thank you! Please come again.")
    sys.exit()

  else:
    print("Please re-enter with y or n")
    user_input()

def search_product(user_fav_list=[]):
  """
  Ask the user what they would like to order, then it plugs the input into the find_search_product helper function which searchs the products in the databse based on regex.
  """
  search_product = input(dedent(
    '''
    What would you like to order?
    '''
  ))
  
  if search_product =='q':
    print("Thank you for shopping here!")
    sys.exit()

  search_product = search_product.lower()

  find_search_product(search_product,user_fav_list)


def find_search_product(search_product, user_fav_list):
    """
    function has a dictionary of regex terms, then it iterates through a list of data and if the regex matches up with the search, it appends the items to user_fav_list.  
    """

    regex_dict = {'mascara':'\w*.ascara\w*', 'foundation': '\w*.oundation\w*', 'eye shadow': '\w*.hadow\w*', 'lip products': '\w*.ip\w*', 'bronzer': '\w*.onzer\w*', 'liner': '\w*[Ll]iner\w*', 'pencil' : '\w*.encil', 'blush' : '\w*.lush', 'cream' : '\w*.ream\w*', 'moisturizer': '\w*.oistu\w*', 'nail': '\w*.ail\w*', 'primer': '\w*.rimer\w*', 'powder': '\w*.owder\w*'}

    pattern = str(regex_dict[search_product])

    vegan_makeup_list = beauty_api_call()

    for item in vegan_makeup_list:
      if re.search(pattern,item['name'].strip()):
        user_fav_list.append(item['name'])
    # user_fav_list=list(set(user_fav_list))

    # print(user_fav_list)

    user_input(user_fav_list)

    save_user_product(user_fav_list)

def save_user_product(user_fav_list):
  """
  A function that will give the user and option to save their searched products.  If the user determines to save the products, it will write the products to a new database, if not, it will discard the products that they have searched.  
  """
  if len(user_fav_list) > 0:
    order_save = input(dedent(
    '''
    Would you like to save your products?
    '''))

    if order_save == 'y':
      with open("./assets/vegan_cosmetics_saved.txt", "w") as file:
        for saved in user_fav_list: 
          file.write(saved + "\n")
    elif order_save == 'n': 
      user_input(user_fav_list)
    elif order_save =='q':
      print("Thank you for shopping here!")
      sys.quit()

def grab_saved_product():
  """
  A function that will print the saved products to be viewed by the user.  
  """
  search_saved_product = input(dedent(
    '''
    Would you like to view your saved products (y/n)?
    '''
  ))

  if search_saved_product == 'y':
    with open("./assets/vegan_cosmetics_saved.txt", "r") as file:
      print(file.read())
    user_choice = input(dedent(
      '''
      Would you like to order more products? Please answer (y/n)
      '''
    ))
    if user_choice == 'y':
      search_product()
    elif user_choice == 'n' or user_choice=='q':
      print("Okay, maybe another time!")
      sys.exit()

  if search_saved_product == 'n':
    print("Okay, maybe another time!")
    sys.exit()
  
if __name__ == "__main__":
    welcome_information()