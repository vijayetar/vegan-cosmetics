from textwrap import dedent
import re
from v_vegan_cosmetics.search_with_api.beauty_api import beauty_api_call
import sys
from v_vegan_cosmetics.web_scraper.web_scraper import get_contents_100percentpure, get_contents_100percentpure_deeper, get_contents_thrive_causemetics, get_contents_thrive_causemetics_deeper
from v_vegan_cosmetics.encrypt_decrypt.encrypt_decrypt import encrypt_password, decrypt_password
from v_vegan_cosmetics.database_peewee.database_peewee import User, FileStorage

## import peewee to create a database for username
from peewee import *

vegan_makeup_list= []
new_user=""

def welcome_information():
  """
  Initial function.  Greets they user and then calls the user_input function which ultimately allows the user to say whether or not they want to order from the store.
  """
  print(dedent('''
  *****************************************

  Welcome to our Vegan Cosmetic Site!!!

  *****************************************
  Press (q) to quit at any time
  *****************************************
  '''))
  get_username_password()

def get_username_password():
  '''Collects User Name and Password and enters new users into database, and checks password with old users'''
  global new_user

  new_user = input(dedent(
    '''
    Please enter user name:
    '''
    ))

  if new_user == "q":
    print("*" * 100)
    print("Thank you for shopping here!")
    print("*" * 100)
    sys.exit()

  new_user_password = input(dedent(
    '''
    Please enter 8 letter password: 
    '''
    ))

  while len(new_user_password) < 8:
    new_user_password = input(dedent(
    '''
    Please enter 8 letter password: 
    '''
    ))

  check_user_in_database(new_user, new_user_password)

  user_input()

def check_user_in_database(new_user, new_user_password):
  '''Function takes in username and password as argument and checks if they match in the database. If not, they are both added to the database as new user'''
  # retrieve data from data base and check if it matches
  for person in User.select():
    if new_user == person.name:
      if new_user_password == decrypt_password(person.password):
        print(f"Welcome Back {new_user}!!!")
        return
      print(f"You have entered a wrong password. Please try again!!!")
      get_username_password()
      return
  new_user = new_user.lower()

  user = User(name = new_user, password = encrypt_password(new_user_password))

  user.save() #added to our database

  print(f"Welcome {new_user}!! You have been added to our database.")

  # creates an empty file for the new user and saves path in the FileStorage database
  file_path_name = f"./assets/user_saved_files/{new_user}_vegan_saved_cosmetics.txt"

  user_file_data = FileStorage.create(owner = user, file_name = file_path_name)

  with open(file_path_name,'w+') as file:
    file.write("")

  return
  

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
    print("*" * 100)
    print("Thank you for shopping here!")
    print("*" * 100)
    sys.exit()

  else:
    print("Please re-enter with (y) or (n)")
    user_input()

def search_product(user_fav_list=[]):
  """
  Ask the user what they would like to order, then it plugs the input into the find_search_product helper function which searchs the products in the databse based on regex.
  """
  print(dedent(
    '''
    These are the categories and individual products available:

    Eye Vegan Products: mascara, eye shadow, liner
    Lip Vegan Products: lip products, liner, pencil
    Face Vegan Products: cream, moisturizer, bronzer, foundation, blush, primer
    Nail Vegan Products: nail

    Please type in either category or product

    '''
  ))
  search_word = input(dedent(
    '''
    What would you like to view? Quit with (q)
    '''
  ))
  
  if search_word =='q':
    print("*" * 100)
    print("Thank you for shopping here!")
    print("*" * 100)
    sys.exit()

  search_word = search_word.lower()

  find_search_product(search_word,user_fav_list)


def find_search_product(search_word, user_fav_list):
    """
    function has a dictionary of regex terms, then it iterates through a list of data and if the regex matches up with the search, it appends the items to user_fav_list.  
    """

    regex_dict = {'mascara':'\w*.ascara\w*', 'foundation': '\w*.oundation\w*', 'eye shadow': '\w*.hadow\w*', 'lip products': '\w*.ip\w*', 'bronzer': '\w*.onzer\w*', 'liner': '\w*[Ll]iner\w*', 'pencil' : '\w*.encil', 'blush' : '\w*.lush', 'cream' : '\w*.ream\w*', 'moisturizer': '\w*.oistu\w*', 'nail': '\w*.ail\w*', 'primer': '\w*.rimer\w*', 'powder': '\w*.owder\w*', 'eye vegan products': '\w*.ascara\w*|\w*.hadow\w*|\w*.[Ll]iner\w*', 'lip vegan products': '\w*.ip\w*|\w*[Ll]iner\w*|\w*.encil', 'face vegan products': '\w*.ream\w*|\w*.oistu\w*|\w*.onzer\w*|\w*.oundation\w*|\w*.lush|\w*.rimer\w*', 'nail vegan products': '\w*.ail\w*'}

    if search_word not in regex_dict:
      search_product(user_fav_list)

    pattern = str(regex_dict[search_word])
    
    global vegan_makeup_list
    if not vegan_makeup_list:
    # API call to makeup_API and the webscraping initiated
      vegan_makeup_list = beauty_api_call()
      # get_contents_100percentpure()
      # get_contents_thrive_causemetics()

    # searching for item in the API
    for item in vegan_makeup_list:
      if re.search(pattern,item['name'].strip()):
        user_fav_list.append(f"Name :   {item['name']}  Cost :    ${item['price']} \n")

    with open ("./assets/thrive_cosmetics_saved.txt", "r") as file:
      thrive_cosmetics_scrape = file.readlines()
    
    with open ("./assets/hundred_percent_saved.txt", "r") as file:
      hundred_percent_scrape = file.readlines()

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
      global new_user
      query = FileStorage.get(FileStorage.owner == User.get(User.name==new_user))
      with open(query.file_name, "a+") as file:
        for saved in user_fav_list: 
          file.write(saved + "\n")
      grab_saved_product()
    elif order_save == 'n': 
      user_input(user_fav_list)
    elif order_save =='q':
      print("*" * 100)
      print("Thank you for shopping here!")
      print("*" * 100)
    else:
      print("Please re-enter with (y) or (n)")
      save_user_product(user_fav_list)

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
    global new_user
    query = FileStorage.get(FileStorage.owner == User.get(User.name==new_user))
    with open(query.file_name, "r") as file:
      saved_user_file = file.read()
    if not saved_user_file:
      print("*" * 100)
      print("There are no saved items in your personal catalog")
      print("*" * 100)
    elif saved_user_file:
      print(saved_user_file)
    else:
      print("Please re-enter with (y) or (n)")
      grab_saved_product()

    user_choice = input(dedent(
      '''
      Would you like to view more products(y) or quit(q)?
      '''
    ))
    if user_choice == 'y':
      search_product()
    elif user_choice == 'n' or user_choice=='q':
      print("*" * 100)
      print("Thank you for shopping here!")
      print("*" * 100)
      sys.exit()

  elif search_saved_product == 'n':
    user_choice = input(dedent(
      '''
      Enter (q) to quit or (y) to view more products 
      '''
    ))
    if user_choice == 'n' or user_choice=='q':
      print("*" * 100)
      print("Thank you for shopping here!")
      print("*" * 100)
      sys.exit()
    search_product()
  else:
    print("Please re-enter with (y) or (n)") 
    grab_saved_product()
      
if __name__ == "__main__":
    welcome_information()
    # for file in FileStorage.select():
    #   file.delete_instance()
    # for person in User.select():
    #   person.delete_instance()



