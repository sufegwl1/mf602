# 
# a1task3.py - Assignment 1, Task 3
# Name: Zuhua Wang
# Email address: zuhuwang@bu.edu
# Description: Functions for time value
# of money calculations
# 
#

def fv_lump_sum(r, n, pv):
    """ return the future value of a lump
        sump pv invested at the periodic
        rate r for n periods.
    """
    return pv * (1 + r) ** n 

def pv_lump_sum(r, n, fv):
    """ return the present value of a lump
        sum fv to be received in the future,
        discounted at the periodic rate r for
        n periods. 
    """
    return fv / (1 + r) ** n

def fv_annuity(r, n, pmt):
    """ return the future value of an
        annuity of pmt to be received
        each period for n periods,
        invested at the periodic rate r. 
    """
    return pmt * (( 1 + r ) ** n - 1) / r 

def pv_annuity(r, n, pmt):
    """ return the present value of an
        annuity of pmt to be received
        each period for n periods,
        discounted at the rate r. 
    """
    return pmt * (1 - (1 + r) ** ( -n )) / r

def annuity_payment(r, n, pv):
    """ return the annuity payment 
        for a present value of pv to be
        repaid at a periodic interest rate
        of r for n periods.
    """
    return r * pv / (1 - (1 + r) ** (-n))
