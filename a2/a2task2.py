# File: a2pr2.py Assignment 2, Problem 2 
#
# Author: Zuhua Wang (zuhuwang@bu.edu), 8/12/2020
#
# Description: 
# 
# Recursion

def mult(n,m):
    """return the product of those integers.
    """
    if n>=0:
        if n==1:
            return m
        else:
            n = n - 1
            return mult(n , m)+m
    else:
        return -mult(-n , m)
    
def copy(s,n):
    """ return a string in which n copies of s have been concatenated together. 
    """
    if n<=0:
        return ""
    if n==1:
        return s
    else:
        rest = copy(s,n-1)
        return rest + s

def double(s):
    """ return the string formed by doubling each character in the string. 
    """
    if s=='':
        return ''
    else:
        return s[0]+s[0]+double(s[1:])
 
def mylen(s):
    """ returns the length of the sequence s
        input: s is a sequence (a string or list)
    """
    if s == '' or s == []:
        return 0
    else:
        len_rest = mylen(s[1:])
        return 1 + len_rest
    
def dot(l1, l2):
    """  return the dot product of those lists
    """
    if mylen(l1)!=mylen(l2):
        return 0.0
    if l1==[] and l2==[]:
        return 0.0
    elif l1!=[] and l2!=[]:
        return l1[0]*l2[0]+dot(l1[1:],l2[1:])
    
def find_min(items):
    """ find the minimum from a list of items.
    """
    if len(items) == 1:
        return items[0]
    else:
        min_in_rest = find_min(items[1:])
        if items[0] < min_in_rest:
            return items[0]
        else:
            return min_in_rest
    
def weave(s1,s2):
    """ return a new string that is formed by "weaving" together the 
        characters in the strings s1 and s2 to create a single string.
    """
    if mylen(s1)==1 and mylen(s2)==1:
        return s1[0]+s2[0]
    
    elif mylen(s1)>1 and mylen(s2)>1:
        return s1[0]+s2[0]+weave(s1[1:],s2[1:])
    elif mylen(s1)>1 and mylen(s2)==1:
        return s1[0]+s2[0]+weave(s1[1:],[])
    elif mylen(s1)==1 and mylen(s2)>1:
        return s1[0]+s2[0]+weave([], s2[1:])
    elif mylen(s1)==0 and mylen(s2)>1:
        return s2[0]+weave(s1,s2[1:])
    elif mylen(s2)==0 and mylen(s1)>1:
        return s1[0]+weave(s1[1:],s2)
    elif mylen(s1)==0 and mylen(s2)==1:
        return s2[0]
    elif mylen(s2)==0 and mylen(s1)==1:
        return s1[0]
    elif mylen(s1)==0 and mylen(s2)==0:
        return ""
    
    
if __name__ == '__main__':
    """ test function for the functions above """
    test1 = mult(6, 7)
    print('the first test returns', test1)
    
    test2 = copy('da', 2)
    print("copy('da', 2) returns",test2)
    
    test3= double('hello')
    print("double('hello') returns",test3)
    
    test4= dot([5, 3], [6, 4]) 
    print("dot([5, 3], [6, 4])  returns",test4)
    
    test5= letters = ['z','h','e','l','m','c','s']
    print("letters = ['z','h','e','l','m','c','s'] returns",test5)
    
    test6= weave('aaaa', 'bbbbbb')
    print("weave('aaaa', 'bbbbbb') returns",test6)
    

    
    
    