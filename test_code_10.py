import os
import sys
import random
from code_10 import get_bubble_sorted_list
from code_10 import get_insert_sorted_list

def check_if_file_exists():
    try:
        exists = os.path.exists("code_10.py")
        assert exists == True
    except:
        sys.exit()

def get_random_list_of_items():
    list_length = random.randint(10,20)
    new_list = []
    for i in range(1,list_length):
        new_list.append(random.randint(100,500))
    return [new_list,sorted(new_list)]

def test_bubble_sort_algorithm():
    check_if_file_exists()
    lists_of_items = get_random_list_of_items()
    test_list = get_bubble_sorted_list(lists_of_items[0])
    assert test_list == lists_of_items[1]
 
def test_insert_sort_algorithm():
    check_if_file_exists()
    lists_of_items = get_random_list_of_items()
    test_list = get_insert_sorted_list(lists_of_items[0])
    assert test_list == lists_of_items[1]