# File: a6pr1.py Assignment 6, Problem 1 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/24/2020
#
# Description: 
#
# Implementing a Matrix as a 2-D List
#

def zeros(n, m=''):
    """ produce zeros matrix
    """
    if m=='':
        m=n
    sublist=[]
    for i in range(m):
        sublist.append(0)
    whole_list=[sublist]
    for i in range(n-1):
        sublist1=sublist.copy()
        whole_list.append(sublist1)
    return whole_list

def print_matrix(m, label=""):
    """ print matrix nicely
    """
    if label!="":
        print (label,"=")
    print ("[",end='')
    for i in m[:-1]:
        print('[',end="")
        for j in i[:-1]:
            print (f'{j:7.2f}',end=', ')
        print (f'{i[-1]:7.2f}',end="]\n ")
    print('[',end="")
    for j in m[-1][:-1]:
        print (f'{j:7.2f}',end=', ')
    print (f'{m[-1][-1]:7.2f}',end="]]\n")
            
#print_matrix([[1,2],[3,4],[5,6]])

def identity_matrix(n):
    """ return I
    """
    i_matrix = zeros(n,n)
    for i in range(n):
        i_matrix[i][i]=1
    return i_matrix

def transpose(M):
    """ return transpose matrix.
    """
    t_matrix=[]
    if type(M[0])==list:
        for i in range(len(M[0])):
            line = []
            for j in range(len(M)):
                line+=[M[j][i]]
            t_matrix+=[line]
    else:
        for i in M:
            t_matrix+=[[i]]
    return t_matrix
           
def swap_rows(M, src, dest):
    """ return swaped matrix.
    """
    assert(len(M)>src and len(M)>dest)
    temp = M[src][:]
    M[src]=M[dest][:]
    M[dest]=temp
    #return M
    
def mult_row_scalar(M, row, scalar):
    """ return matrix after mult
    """
    for i in range(len(M[0])):
        M[row][i]*=scalar
    
def add_row_into(M, src, dest):
    """ return matrix after addition.
    """
    for i in range(len(M[0])):
        M[dest][i]+=M[src][i]
    
                

#print (zeros(2,2))
#print_matrix(zeros(4,2),"a")
