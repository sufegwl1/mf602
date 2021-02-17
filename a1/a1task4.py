# 
# a1task4.py - Assignment 1, Task 4
# Name: Zuhua Wang
# Email address: zuhuwang@bu.edu
# Description: The Life-Cycle Model
# of Saving and Consumption
# 
#

from a1task3 import *


# greeting 
print('Welcome to the Life-Cycle Sustainable Spending Calculator.\n')
    
def life_cycle_model():
    """ calculate the sustainable (smooth) amount of spending for each year of life until
	some maximum age.
    """
    # ask for information
    r = float(input("Enter the current inflation-indexed risk-free rate of return: "))
    age_now = int(input("Enter your age now: "))
    retirement_age=int(input("Enter your expected retirement age: "))
    income=int(input("Enter your current annual income: "))
    
    # calculate remaining working years and print
    remaining_working_years = retirement_age - age_now
    print("\nYou have", remaining_working_years, 
          'remaining working years with an income of $'+str(income),"per year.")
    
    # calculate present value and print
    present_value = pv_annuity(r, remaining_working_years, income)
    print ("The present value of your human capital is about $" +
           str(int(present_value)))
    
    # ask for the value of financial assets
    financial_assets = int(input("Enter the value of your financial assets: "))
    
    # calculate the economic net worth
    economic_net_worth = financial_assets + present_value
    
    # print the economic net worth
    print ("Your economic net worth is : $"+str(int(economic_net_worth))+"\n")
    
    # calculate and print sustainable standard of living 
    sustainable_standard_of_living = annuity_payment(r, 100-age_now, economic_net_worth)
    
    print("Your sustainable standard of living is about $" 
          + str(int(sustainable_standard_of_living)) + "per year.")
    
    # calculate and print saving
    savings = income - sustainable_standard_of_living
    print ("To achieve this atandard of living to age 100, you must save $"
           + str(int(savings)) + " per year.")
    
if __name__ == '__main__':

        life_cycle_model()