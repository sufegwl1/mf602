# File: a2pr1.py Assignment 2, Problem 1 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/12/2020
#
# Description: 
# 
# Decision Statements
#

def smaller(x , y):
    """ returns the smaller of the two numbers.
    """
    if x <= y:
        return x
    return y

def smallest(x, y, z):
    """ returns the smallest of the three.
    """
    return smaller(smaller(x, y),z)

def is_factor(n, x):
    """ returns True if x is a factor of n and False otherwise.
    """
    return n % x == 0

def has_vowel(s):
    """ returns True if the string contains at least one vowel
        (any letter in 'aeiou') and False otherwise.
    """
    if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
        return True
    return False