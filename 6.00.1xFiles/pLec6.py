## Week 3 Sequences

## divisors

def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    total += d
print(total)

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
     
## universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)


def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)

def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)

# applyToEach

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)
