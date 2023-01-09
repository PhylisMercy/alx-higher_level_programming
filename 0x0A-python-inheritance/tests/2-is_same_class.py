#!/usr/bin/python3                                                                                                              
# -*- coding: utf-8 -*-                                                                                                         
"""                                                                                                                             
Created on Monday January 9 6:52:37 2023                                                                                        
@author: Phylis Mercy                                                                                                           
""" 


def is_same_class(obj, a_class):
    """
    Checks if two objects are the same class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
