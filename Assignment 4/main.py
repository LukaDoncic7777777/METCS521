# 3
# (a)
def firsthalf(S):
    print(S[0:len(S) // 2])


# (b)
def secondhalf(S):
    print(S[len(S) // 2:len(S)])


# 4
# (a)
def middlechar(S):
    print(S[len(S) // 2])


# (b)
def firstone(S):
    print(S[0:(len(S) // 2)])


# (c)
def secondone(S):
    print(S[len(S) // 2 + 1:len(S)])


# 30
def findtheletter(S):
    x = S.find('o')
    y = S.find('o', 4, len(S))
    print(x)
    print(y)


# 31
def convertbackward(S):
    x = S[0:7]
    y = S[9:len(S)]
    converted = y + " " + x
    print(converted)


# 42
def compare_two_string(a, b):
    if len(a) > len(b):
        print(b)


import string


# 44
def convert_sentence(S):
    upperchar, lowerchar, digits, punct = 0, 0, 0, 0
    for i in range(len(S)):
        if S[i].isupper():
            upperchar += 1
        if S[i].islower():
            lowerchar += 1
        if S[i].isdigit():
            digits += 1
        if S[i] in string.punctuation:
            punct += 1

    print(f"Upper Characters: {upperchar}")
    print(f"Lower Characters: {lowerchar}")
    print(f"Digit Numbers: {digits}")
    print(f"Punctuations: {punct}")


# 47
def createpassword():
    x = input("Please enter your password: ")
    checklength = False
    checkdigit = False
    checklower = False
    checkupper = False

    for a in x:
        if 6 <= len(x) <= 20:
            checklength = True
        if a.isdigit():
            checkdigit = True
        if a.islower():
            checklower = True
        if a.isupper():
            checkupper = True
    if checkupper and checklower and checkdigit and checklength:
        print("This is a valid password")
    else:
        print("This is an invalid password")


# 50
def findallvowels():
    x = input("Please enter a string: ")
    temp = ""
    tempchar = set()
    trial = 0
    for a in x:
        trial += 1
        if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
            tempchar.add(a.lower())
        if 'a' in tempchar and 'e' in tempchar and 'i' in tempchar and 'o' in tempchar and 'u' in tempchar:
            break
    for b in tempchar:
        temp += b

    print(trial)


import random


# 51
def fixsentence():
    x = input("Please enter a sentence: ")
    if x[0].islower():
        a = x[0].upper()
        print("First letter is not capitalized")
        print(a + x[1:len(x)])
    if x[len(x) - 1] not in string.punctuation:
        b = '.'
        print("Last letter is not a punctuation mark")
        print(x[0].upper() + x[1:len(x)] + b)
    else:
        print(x)


#52
def threedigit():
    while True:
        try:
            number = int(input("Enter a 3-digit number: "))
            s = str(number)
            valid = (len(s) == 3)
            for i in range(1, len(s)):
                if s[i] < s[i - 1]:
                    valid = False
            if valid:
                break
        except:
            pass
        print("Invalid number. Try again!")
    print("Valid number = " + str(number))




threedigit()


