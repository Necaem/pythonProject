## Week 3 Recursivity

def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp == 0:
        return 1
    else:   
        while exp > 0:
            result *= base
            exp -= 1
        return result
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    
    retruns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
        
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp%2 == 0:
        base = recurPowerNew(base*base, exp/2)
    else:
        base = base * recurPowerNew(base, exp - 1)
    return base

def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)        
        
def factI(n):
    """assumes that n is an int > 0
       returns n!"""
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def factR(n):
    """assumes that n is an int > 0
       returns n!"""
    if n == 1:
        return n
    return n*factR(n-1)        
    
def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    result = min(a,b)
    while result > 1:
        if a%result == 0 and b%result == 0:
            return result
        else:
            result = result - 1
    return result
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
        
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
    
def lenIter(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''

    result = 0
    for letter in aStr:
        result = result + 1
    return result



def lenRecur(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''

    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    This example uses the bisection search algorithm.
    '''

    mid = len(aStr)/2
    if aStr == '' or len(aStr) == 1:
        return char == aStr
    elif char == aStr[mid]:
            return True
    elif char < aStr[mid]:
        aStr = aStr[: mid]
        return isIn(char, aStr)
    else:
        aStr = aStr[mid + 1:]
        return isIn(char, aStr)



def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''

    return aTup[0::2]



def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''

    count = 0
    for i in aDict:
     count = count + len(aDict[i])
    return count



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''

    if aDict:
     return max(aDict.items(), key=lambda x: len(x[1]))[0]
    
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    
    '''
    #base case
    if len(str1) != len(str2):
        return False
    if len(str1) == 1: #antistica o nikos to theorise gia str1 ="" einai to base case mou:an den to valw tote molis kata to 
        #recursive call ellatothei to str1,str2 se = "", tha paei na ksanakalesei to recursive call
        #kai tote string index out of range!. Einai gia na tou pw where to stop!!!!!
        return str1[0] == str2[-1]
    else:
        print 'first char of current str1[0]=',str1[0]
        print 'last char of current str2[-1]=',str2[-1]
        print 'str1=',str1[1:]
        print 'str2=',str2[:-1]
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])