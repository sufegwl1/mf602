# File: a4pr2.py Assignment 4, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/19/2020
#
# Description: 
#
# Simulating a Bond Auction
#
from a4task1 import *
def collect_bids(filename):
    """
    reutrn bids from file
    """
    f = open(filename)
    f.readline()
    bids = []
    for line in f:
        line = line[:-1]
        line_list = line.split(',')
        line_list[1] = int(line_list[1])
        line_list[2] = float(line_list[2])   
        line_list[0] = int(line_list[0])

        bids.append(line_list)
    f.close()
    return bids

def print_bids(bids):
    """ print bids from 2*2 list
    """
    print (f'{"   Bid ID":8}{"      Bid Amount":18}{"   Price":10}')
    for bid in bids:
        print (f'       {bid[0]:8}${bid[1]:12}${bid[2]:10}')
        
def find_winning_bids(bids, total_offering_fv, c,n,m):
    """ processes a list of bids and determine which are
        successful in the auction.
    """
    sort=sorted(bids, key=lambda x:x[2],reverse=True)
    print('Here are all of the bids, sorted by price descending:')
    print_bids(sort)
    #print(f'\nThe auction is for ${total_offering_fv:.2f} of bonds.\n')
    count = 0
    #last_bid_amount = 0
    last_bid_price=0
    start=0
    sold = []
    for bid in sort:
        if total_offering_fv > bid[1]:
            total_offering_fv = total_offering_fv - bid[1]
            count = count + 1
            #bid[1] = int(bid[1]
            sold = sold + bid
        elif total_offering_fv == bid[1]:
            total_offering_fv = 0
            last_bid_price = bid[1]
            #bid[1] = int(bid[1])
            count = count + 1
            start = 1
            sold = sold + bid
        elif total_offering_fv < bid[1] and start == 0:
            last_bid_price=bid[2]
            #last_bid_amount=bid[1]
            bid[1] = total_offering_fv
            
            total_offering_fv = total_offering_fv - bid[1]
            count = count +1
            start = 1
            sold = sold + bid
        elif total_offering_fv < int(bid[1]) and start == 1:
            bid[1] =0
            total_offering_fv = total_offering_fv - int(bid[1])
        bid[0] = str(bid[0])
        #bid[1] = str(bid[1])
        bid[2] = str(bid[2])
            
    print(count,'bids were successful in the auction.')
    print(f"The auction clearing price was ${str(last_bid_price)}, i.e., YTM is {str(bond_yield_to_maturity(100, c, n,m,float(last_bid_price))):.5} per year.")
    print("Here are the results for all bids:")
    print_bids(sort)
    return sold


if __name__ == '__main__':

    # read in the bids
    bids = collect_bids('./bond_bids.csv')
    print("Here are all the bids:")
    print_bids(bids)
    print()

    # process the bids in an auction of $1,400,000 of 5-year 3.25% semi-annual coupon bonds
    processed_bids = find_winning_bids(bids, 1400000, 0.0325, 5, 2)
    