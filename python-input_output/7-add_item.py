#!/usr/bin/python3
""""Adds all arguments to a Python list, and saves them to a file."""
import sys
import json
import os.path
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file
def add_item(args):
    """Adds all arguments to a Python list, and saves them to a file."""
    filename = "add_item.json"
    
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []
    
    items.extend(args)
    
    save_to_json_file(items, filename)