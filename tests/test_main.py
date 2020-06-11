from main import welcome_information, user_input, search_product, find_search_product
from textwrap import dedent
import re
from tests.flo import Flo
import pytest

def test_flo_quit():
    Flo.test('tests/flow/flo_quit.txt')

def test_flo_order_quit():
    Flo.test('tests/flow/flo_order_quit.txt')

def test_flo_order_bad_quit():
    Flo.test('tests/flow/flo_order_bad_quit.txt')

def test_flo_order_mascara_no_view_quit():
    Flo.test('tests/flow/flo_order_mascara_no_view_quit.txt')

def test_flo_no_order_no_view_quit():
    Flo.test('tests/flow/flo_no_order_no_view_quit.txt')

def test_flo_order_mascara_cream_no_view_quit():
    Flo.test('tests/flow/flo_order_mascara_cream_no_view.txt')

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



