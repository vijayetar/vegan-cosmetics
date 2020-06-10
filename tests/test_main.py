from main import welcome_information, user_input, search_product, find_search_product
from textwrap import dedent
import re
from tests.flo import Flo
import pytest

# def test_flo_quit():
#     Flo.test('tests/flow/flo_quit.txt')
# # def test_flo_order_mascara_then_quit():
# #     Flo.test('tests/flow/flo_order_mascara_then_quit.txt')

# def test_user_input():
#     user_input()
#     expected = "Thank you! Please come again. "
#     actual = "Thank you! Please come again. "
#     assert actual == expected

# def test_bad_user_input():
#     user_input()
#     expected = "Please re-enter with y or n"
#     actual = "Please re-enter with y or n"
#     assert actual==expected

# def test_welcome_information():
#     welcome_information()
#     actual = print(dedent('''
#   *****************************************

#   Welcome to our Vegan Cosmetic Site!!!

#   *****************************************

#   Press (q) to quit at any time
#   '''))
#     expected = print('asdfdasf')
#     assert actual == expected

def test_regex_found():
    with open('./assets/fake_item_list.txt', 'r') as f:
        item_string = f.read().strip()
    pattern = '\w*.ascara\w*'
    actual = re.findall(pattern, item_string)
    expected = ['Mascara', 'Mascara', 'Mascara', 'Mascara', 'Mascara', 'Mascara']
    assert actual == expected
        
def test_regex_not_found():
    with open('./assets/fake_item_list.txt', 'r') as f:
        item_string = f.read().strip()
    pattern = '\w*.ipod\w*'
    actual = re.findall(pattern, item_string)
    expected = []
    assert actual == expected



