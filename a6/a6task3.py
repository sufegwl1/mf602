# File: a6pr3.py Assignment 6, Problem 3 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/26/2020
#
# Description: 
#
# Matrix Application: Bond Pricing
#
from a4task1 import discount_factors, bond_cashflows # bond functions
from a6task1 import *
from a6task2 import *

def bond_price(fv, c, n,m ,r):
    """ return bond price.
    """
    D = discount_factors(r,n,m)
    CF=bond_cashflows(fv, c,n,m)
    #print(D)
    #print(CF)
    #return 1
    #print(transpose(CF))
    return dot_product(D, transpose(CF))

def bootstrap(cashflows, prices):
    """ bootstrap
    """
    return dot_product(inverse_matrix(cashflows),prices)
    
    """

CF = [[105,0,0],[6,106,0],[7,7,107]]
P = [[99.5], [101.25], [100.35]]
D = bootstrap(CF, P)
print_matrix(CF, 'Bond Cashflows')
print_matrix(P, 'Bond Prices')
print_matrix(D, 'Implied Discount Factors') 

print(D)
"""























