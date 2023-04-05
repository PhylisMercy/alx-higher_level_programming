#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri April 7 07:42 2023
@author: Phylis Mercy
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
