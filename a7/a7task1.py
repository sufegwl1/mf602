# File: a7pr1.py Assignment 7, Problem 1 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/27/2020
#
# Description: 
#
# A Date class
#

class Date:
    """ Date class
    """
    def __init__(self, new_month, new_day, new_year):
        """ initial a new date
        """
        self.month = new_month
        self.day = new_day
        self.year = new_year
        
    def __repr__(self):
        """ return the date in a nice format
        """
        return str(self.month).zfill(2)+'/'+str(self.day).zfill(2)+'/'+str(self.year)
    
    