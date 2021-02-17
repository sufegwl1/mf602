# File: a4pr2.py Assignment 6, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/26/2020
#
# Description: 
#
# Matrix Operations
#

from a6task1 import *

def add_matrices(A, B):
    """ return addition of two matrices.
    """
    assert(len(A[0]) == len(B[0]))
    temp = A +B
    for i in range(len(A)):
        add_row_into(temp , i , i+len(A))
    return temp[len(A):]
    
    #print_matrix(temp)

def sub_matrices(A, B):
    """ return result of A-B
    """
    assert(len(A[0]) == len(B[0]))
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] *= -1
    return add_matrices(A, B)

def mult_scalar(M, s):
    """ return result of M*s.
    """
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] *= s
    return M

def dot_product(M, N):
    """ return dot product
    """
    if type(M[0])==list:
        assert(len(M[0]) == len(N))
        new = zeros(len(M), len(N[0]))
        for i in range(len(M)):
            for j in range(len(N[0])):
                for k in range(len(M[0])):
                    new[i][j]+=(M[i][k]*N[k][j])
    else:
        new = 0
        #print (M)
        #print (N)
        for i in range(len(M)):
            temp=  M[i]* N[i][0]
            new += temp
    return new

def create_sub_matrix(M, exclude_row, exclude_col):
    ''' return matrix after minus one row and one column.
    '''
    temp=[]
    for i in M:
        temp.append(i[:])
    temp.pop(exclude_row)
    for i in temp:
        i.pop(exclude_col)
    return temp

def determinant(M):
    ''' return determent of M
    '''
    assert(len(M[0]) == len(M))
    if len(M)==2:
        return M[0][0]*M[1][1]-M[0][1]*M[1][0]
    elif len(M)>2:
        answer = 0
        for i in range(len(M[0])):
            if i%2==0:
                answer = answer + M[0][i]*determinant(create_sub_matrix(M, 0, i))
            else:
                answer = answer - M[0][i]*determinant(create_sub_matrix(M, 0, i))
        return answer
    else:
        return M[0][0]


def matrix_of_minors(M):
    """ return minors of M
    """
    temp = zeros(len(M),len(M[0]))
    for i in range(len(M)):
        for j in range(len(M[i])):
            temp[i][j] = determinant(create_sub_matrix(M, i, j))
    return temp

def inverse_matrix(M):
    """ return inverse matrix.
    """
    temp = matrix_of_minors(M)
    #print_matrix(temp)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if (i%2==0 and j%2==1):
                temp[i][j] *= -1
            if (i%2==1 and j%2==0):
                temp[i][j] *= -1
    #print_matrix(temp)
    t = transpose(temp)
    #print()
    print_matrix(t)
    #print(determinant(M))
    return mult_scalar(t,1.0/determinant(M))

"""
A = [[3,2,0,1],[4,0,1,2],[3,0,2,1],[9,2,3,1]]
print_matrix(A, 'A')
print(determinant(A))

AI = inverse_matrix(A)
print_matrix(AI, 'AI')
DP = dot_product(A,AI)
print_matrix(DP)
"""

"""
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(create_sub_matrix(A, 0, 0))
print_matrix(create_sub_matrix(A, 2, 3))
"""


'''
A = [[1,2,3],[4,5,6]]
B = [[3,2],[4,1],[5,0]]
P = dot_product(A,B)
print_matrix(P, 'P')
'''



