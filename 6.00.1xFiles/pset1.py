## 6.00.1x Problem Set 1
# COUNTING VOWELS   

def countVowels(s):
    vowels = 0
    vowels += s.count('a')
    vowels += s.count('e')
    vowels += s.count('i')
    vowels += s.count('o')
    vowels += s.count('u')
    return vowels
#print "Number of vowels: " + str(countVowels(s))

def countBobs(s):
    bobs = 0
    bobs += s.find('bob')
    return bobs
#print "Number of times bob occurs is: "+str(countBobs(s))

def alphSub(s):
    groups = []
    cur_longest = ''
    prev_char = ''
    for c in s:
        if prev_char and c < prev_char:
            groups.append(cur_longest)
            cur_longest = c
        else:
            cur_longest += c
        prev_char = c
    groups.append(cur_longest)
    cur_longest = c
    return max(groups, key=len)