##########################
# Quiz 1 Problem 5
##########################
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    bList = []
    for thing in aList:
        if len(thing) < 4:
            bList.apped(thing)
    return bList

##########################        
# Quiz 1 Problem 6
##########################
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N <= 0:
        return 0
    else:
        return (N%10) + sumDigits(N/10)
        
##########################        
# Quiz 1 Problem 7     
##########################   
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    listA = []
    d = dict((k,v) for k, v in aDict.items() if v == target)
    listA = d.keys()
    return listA
    
##########################            
# Quiz 1 Problem 8 
##########################    
L = ['a', 'b', 'a']
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    for i in range(len(L)-1,-1,-1):
        if f(L[i]) == False:
            del L[i] 
            # Should start deleting from the back
    return len(L)
    
def f(s):
    return 'a' in s
      


