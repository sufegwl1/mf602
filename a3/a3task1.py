# File: a2pr2.py Assignment 2, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/12/2020
#
# Description: 
#
# Descriptive Statistics
#
#
def mean(values):
    """ return means
    """
    return sum(values)/len(values)
 
def variance(values):
    """return variance
    """
    sum = 0.0
    for a in values:
        sum += ( a - mean(values)) ** 2
    return sum/len(values)

def stdev(values):
    """ return standard deviation
    """
    return variance(values) ** 0.5

def covariance(x,y):
    """ return the covariance
    """
    sum = 0.0
    for a in range(0,len(x)):
        sum += ( x[a] - mean(x)) * (y[a] - mean(y))
    return sum/len(x)

def correlation(x,y):
    """ return the correlation
    """
    return covariance(x, y)/(stdev(x)*stdev(y))

def rsq(x,y):
    """ return the square of the correlation
    """
    return correlation(x,y)**2

def simple_regression(x,y):
    """ return the regression coefficients
    between these data series
    """
    return [mean(y)-covariance(x,y)/covariance(x,x)*mean(x),covariance(x,y)/covariance(x,x)]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    