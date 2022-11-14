# 13
with open('engmix.txt', 'r', encoding="ISO-8859-1") as fd:
    words = fd.read().splitlines()
from collections import deque
def compoundword():
    d = deque()
    tuple1 = []
    for word in words:
        tuple1.append(word)
        d.append(word)

    for word in tuple1:
        for i in range(len(word)):
            word.strip()
            s1 = word[0:i]
            s2 = word[i:len(word)]
            s1.strip()
            s2.strip()
            if (s1 in words) and (s2 in words):
                print(word + " = " + s1 + " + " + s2)



import math

#15
def promptequation(a, b, c, x, y, radius):
    try:
        dist = ((abs(a * x + b * y + c)) / math.sqrt(a * a + b * b))
        if radius > dist:
            print("Two Intersects")
        elif radius == dist:
            print("One Intersects")
        else:
            print("Do not Intersect")

    except:
        print("Intersect is negative")


#15(a)
def checktwopalin(a, b):
    alist = []
    blist = []
    for n in a:
        alist.append(n)

    for n in b:
        blist.append(n)

    alist.reverse()
    if alist == blist:
        return True

    else:
        return False



#15(b)
def checkthepalin(a, b):
    if checktwopalin(a, b):
        print("This two strings are palindromes")
    else:
        print("They are not palindrome")




#15(c)
def improvedpalin(a, b):
    alist = []
    blist = []

    for n in a.strip():
        alist.append(n.lower())

    for n in b.strip():
        blist.append(n.lower())

    alist.reverse()
    if alist == blist:
        return True

    else:
        return False



#16
def checksort(s):
    test_s = s[:]
    test_s.sort()
    if test_s == s:
        return True
    else:
        return False



#17(a)
def removeeven(s):
    alist = []
    for num in s:
        if (num % 2) != 0:
            alist.append(num)
    return alist

#17(b)
def removeodd(s):
    alist = []
    for num in s:
        if (num % 2) == 0:
            alist.append(num)
    return alist


#17(c):
def removewhatever(s, t):
    alist = []
    if t:
        for num in s:
            if (num % 2) == 0:
                alist.append(num)

    else:
        for num in s:
            if (num % 2) != 0:
                alist.append(num)

    return alist

#19(a)
def multi_find(some_string, sub_string):
    start, end = 0, len(some_string)
    index_store = []
    n = len(sub_string)
    while start < end:
        if some_string[start:start + n] == sub_string:
            index_store.append([start, start + n])
        start += 1

    return index_store


#19(b)
def find_substring(some_string, sub_string):
    if multi_find(some_string, sub_string):
        return True

    else:
        return False



#11(a)
def encryptlanguage(s):
    alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    blist = ['c', 'd', 'e', 'f', 'g', 'h', 'i']
    empty = []
    result = dict(zip(alist, blist))
    for n in s:
        if n == ' ':
            empty.append(n)
            continue
        if n in alist:
            n = result[n]
            empty.append(n)
        else:
            empty.append(n)

    return "".join(empty)



def decript(language):
    blist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    alist = ['c', 'd', 'e', 'f', 'g', 'h', 'i']
    empty = []
    result = dict(zip(alist, blist))
    for n in language:
        if n == ' ':
            empty.append(n)
            continue
        if n in alist:
            n = result[n]
            empty.append(n)
        else:
            empty.append(n)

    return "".join(empty)

#11(b)
def encryptordecript(s, action):
    if action == "encrypt":
        return encryptlanguage(s)
    elif action == "decrypt":
        return decript(s)



#15(a)
def firstone(firstname, lastname):
    alist = []

    for n in firstname:
        alist.append(n)

    for n in lastname:
        alist.append(n)

    return alist



#15(b)
def secondone(firstname, lastname):
    alist = set()
    blist = set()
    for n in firstname:
        if n in alist:
            blist.add(n.lower())
        else:
            alist.add(n.lower())

    for n in lastname:
        if n in alist:
            blist.add(n.lower())
        else:
            alist.add(n.lower())

    return blist


#15(c)
def thirdone(firstname, lastname):
    alist = set()
    blist = set()
    for n in firstname:
        alist.add(n)
    for n in lastname:
        blist.add(n)
    result = alist.symmetric_difference(blist)
    return result


#16
def capitaldict():
    countries = dict()
    n = int(input("How many countries are there: "))
    for i in range(n):
        a = input("Please enter your country: ")
        b = input("Please enter your capital: ")
        countries[a] = b
    for i in sorted(countries.values()):
        print(i, end=" ")



#28
with open('engmix.txt', 'r', encoding="ISO-8859-1") as fd:
    words = fd.read().splitlines()

from collections import defaultdict

def anagram_print(word_list):
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)

    result = {fp: result[fp] for fp in result if len(result[fp]) > 1}
    return result



