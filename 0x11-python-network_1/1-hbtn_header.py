#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed April 5 07:22 2023
@author: Phylis Mercy
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
