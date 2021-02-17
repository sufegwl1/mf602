# File: a2pr2.py Assignment 2, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/12/2020
#
# Description: 
#
# Stock returns and satistics
#
#
from a3task1 import *
#import sys

def calc_returns(prices):
    """ return the periodic returns
    """
    returns=[]
    for i in range(0, len(prices)-1):
        #print(i)
        temp = (prices[i+1]-prices[i])/prices[i]
        returns.append(temp)
    return returns

def process_stock_prices_csv(filename):
    """ return the price
    """
    price=[]
    f = open(filename)
    f.readline()
    for line in f:
        #print(line)
        line = line[:-1]
        sep = line.split(',')
        price.append(float(sep[5]))
    f.close()
    return price

def stock_report(filename):
    """ client program to process stock prices 
        and display descriptive statistics about the
        stocks.
    """
    string = f'Calculated returns for {len(filename)} stocks.'
    string += "\n\nDescriptive statistics for daily stock returns:\n"
    string += "Symbol:        "
    data = []
    for items in filename:
        string += items.split('.')[0]
        #string += items
        string += "      "
        data.append(calc_returns(process_stock_prices_csv(items)))
    result = []
    for company in data:
        company_data=[mean(company),stdev(company),covariance(company,data[-1]),correlation(company,data[-1]),rsq(company, data[-1]),simple_regression(company,data[-1])[1],simple_regression(company,data[-1])[0] ]
        result.append(company_data)
    string += "\nMean:     "
    for i in range(0,len(filename)):
        string += f'{result[i][0]:10.5f}'
    string += "\nStDev:    "
    for i in range(0,len(filename)):
        string += f'{result[i][1]:10.5f}'
    string += "\nCovar:    "
    for i in range(0,len(filename)):
        string += f'{result[i][2]:10.5f}'
    string += "\nCorrel:   "
    for i in range(0,len(filename)):
        string += f'{result[i][3]:10.5f}'
    string += "\nR-SQ:     "
    for i in range(0,len(filename)):
        string += f'{result[i][4]:10.5f}'
    string += "\nBeta:     "
    for i in range(0,len(filename)):
        string += f'{result[i][5]:10.5f}'
    string += "\nAlpha:    "
    for i in range(0,len(filename)):
        string += f'{result[i][6]:10.5f}'
    
    return string
    