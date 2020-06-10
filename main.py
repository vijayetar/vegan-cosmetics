from textwrap import dedent
import re
from vegan_cosmetics.search_with_api.beauty_api import beauty_api_call
import sys
from vegan_cosmetics.web_scraper.web_scraper import get_contents_100percentpure, get_contents_100percentpure_deeper, get_contents_thrive_causemetics, get_contents_thrive_causemetics_deeper

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
  reset_user_saved_file()
  user_input()

def reset_user_saved_file():
  """
  Function that resets the saved users file
  """
  with open("./assets/vegan_cosmetics_saved.txt", "w") as file:
      file.write("")

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
  Would you like to see anything from our store catalog (y/n) Or would you like to quit (q)?
  '''))

  if order_now == 'y':
    search_product(user_fav_list)

  elif order_now == 'n':
    grab_saved_product()

  elif order_now == 'q':
    print("Thank you! Please come again.")
    sys.exit()

  else:
    print("Please re-enter with (y) or (n)")
    user_input()

def search_product(user_fav_list=[]):
  """
  Ask the user what they would like to order, then it plugs the input into the find_search_product helper function which searchs the products in the databse based on regex.
  """
  search_product = input(dedent(
    '''
    What would you like to view? Quit with (q)
    Your options are: 
    Eye Vegan Products: mascara, eye shadow, liner
    Lip Vegan Products: lip products, liner, pencil
    Face Vegan Products: cream, moisturizer, bronzer, foundation, blush, primer
    Nail Vegan Products: nail

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

    # API call to makeup_API and the webscraping initiated
    vegan_makeup_list = beauty_api_call()
    get_contents_100percentpure()
    get_contents_thrive_causemetics()

    with open ("./assets/thrive_cosmetics_saved.txt", "r") as file:
      thrive_cosmetics_scrape = file.readlines()
    
    with open ("./assets/hundred_percent_saved.txt", "r") as file:
      hundred_percent_scrape = file.readlines()
    
    # searching for item in the API
    for item in vegan_makeup_list:
      if re.search(pattern,item['name'].strip()):
        user_fav_list.append(f"Name :   {item['name']}  Cost :    {item['price']} \n")

    # searching for item in the thrive causemetics
    for item in thrive_cosmetics_scrape:
      if re.search(pattern,item.strip()):
        user_fav_list.append(item)
    
    # searching for item in the hundred percent pure
    for item in hundred_percent_scrape:
      if re.search(pattern,item.strip()):
        user_fav_list.append(item)

    # user_input(user_fav_list)
    save_user_product(user_fav_list)

def save_user_product(user_fav_list):
  """
  A function that will give the user and option to save their searched products.  If the user determines to save the products, it will write the products to a new database, if not, it will discard the products that they have searched.  
  """
  if len(user_fav_list) > 0:
    order_save = input(dedent(
    '''
    Would you like to save the products to your personal catalog (y/n)? You can also quit(q)
    '''))

    if order_save == 'y':
      with open("./assets/vegan_cosmetics_saved.txt", "a+") as file:
        for saved in user_fav_list: 
          file.write(saved + "\n")
      grab_saved_product()
    elif order_save == 'n': 
      user_input(user_fav_list)
    elif order_save =='q':
      print("Thank you for shopping here!")
      sys.exit()

def grab_saved_product():
  """
  A function that will print the saved products to be viewed by the user.  
  """
  search_saved_product = input(dedent(
    '''
    Would you like to view your personal catalog (y/n)? You can also quit (q)
    '''
  ))

  if search_saved_product == 'y':
    with open("./assets/vegan_cosmetics_saved.txt", "r") as file:
      saved_user_file = file.read()
    if not saved_user_file:
      print("*" * 100)
      print("There are no saved items in your personal catalog")
      print("*" * 100)
    elif saved_user_file:
      print(saved_user_file)
    user_choice = input(dedent(
      '''
      Would you like to view more products(y/n) or quit(q)?
      '''
    ))
    if user_choice == 'y':
      search_product()
    elif user_choice == 'n' or user_choice=='q':
      print("Thank you for shopping here!")
      sys.exit()
  elif search_saved_product == 'n':
    user_choice = input(dedent(
      '''
      Enter (q) to quit or (y) to view more products 
      '''
    ))
    if user_choice == 'n' or user_choice=='q':
      print("Thank you for shopping here!")
      sys.exit()
    search_product()
     
if __name__ == "__main__":
    welcome_information()