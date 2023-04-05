#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed April 5 07:39 2023
@author: Phylis Mercy
"""
from requests import get


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(bytes_content), bytes_content)
    print(string)
