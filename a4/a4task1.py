# File: a4pr1.py Assignment 4, Problem 1 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/12/2020
#
# Description: 
#
# Discounted Cashflows and Bond Pricing
#
#
def cashflow_times(n, m):
    """ return n year bond with m coupons/year
    """
    return [i for i in range(m * n+1) if i != 0 ]

def discount_factors(r,n,m):
    """ return a list of discount factors
    """
    return [1/((1+r/m)**i) for i in cashflow_times(n,m)]

def bond_cashflows(fv, c, n, m):
    """ return a list of cashflows for a bond specified
        by the parameters.
    """
    #front_cashflow = [fv*c/m for i in cashflow_time if i != 1]
    return [fv*c/m for i in cashflow_times(n,m) if i != 1]+[fv*c/m+fv]

def bond_price(fv, c,n,m,r):
    """ return the price of a bond.
    """
    return sum([a*b for a,b in zip(discount_factors(r,n,m),bond_cashflows(fv, c, n, m))])

def bond_yield_to_maturity(fv, c, n,m,price):
    """ return the rate
    """
    ACCURACY = 0.0001
    positive = 1
    r=0.5
    print (bond_price(fv,c,n,m,0.1))
    """if price>bond_price(fv,c,n,m,0.000001):
        positive = 1
        r=0.5"""
    while positive ==1:
        diff = bond_price(fv,c,n,m,r)-price
        
        if diff < -ACCURACY:
            r=r/2
        elif diff > ACCURACY:
            r=r*1.5
        else:
            return r
    """while positive == 0 :
        diff = -(bond_price(fv,c,n,m,r)-price)
        
        if diff < -ACCURACY:
            r=r/2
        elif diff > ACCURACY:
            r=r*1.5
        else:
            return r
"""






