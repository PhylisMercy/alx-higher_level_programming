#!/usr/bin/python3                                                                                                              
# -*- coding: utf-8 -*-                                                                                                         
""" 
Created on Tuesday January 10 6:10:37 2023  

@author: Phylis Mercy
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save object to a file
    Arguments:
        my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file
    Return:
        A file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
