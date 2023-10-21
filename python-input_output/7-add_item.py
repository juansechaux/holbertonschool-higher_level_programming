#!/usr/bin/python3
"""Module that creates an Object from a “JSON file”.
"""
import json
import sys
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if exists('add_item.json'):
    my_file = load_from_json_file('add_item.json')
    save_to_json_file((my_file + sys.argv[1:]), 'add_item.json')
else:
    save_to_json_file(sys.argv[1:], 'add_item.json')
