#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri April 7 07:45 2023
@author: Phylis Mercy
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
    print(response.text)

