#!/usr/bin/env python3
""" sterializing module that adds the functionality to serialize dict"""

import json


def serialize_and_save_to_file(data, filename):
""" serialize python dic to json file"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
"""  deserialize data from the json file"""
    with open(dilename, 'r', encoding='utf-8') as f:
        return jason.load(f)
