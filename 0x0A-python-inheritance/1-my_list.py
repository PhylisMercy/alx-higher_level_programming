#!/usr/bin/python3                                                                                                              
# -*- coding: utf-8 -*-                                                                                                         
"""                                                                                                                             
Created on Monday January 9 6:52:37 2023                                                                                        
@author: Phylis Mercy                                                                                                           
""" 

class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
