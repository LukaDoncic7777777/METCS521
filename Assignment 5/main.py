# 9
import string


def printallconsonent():
    x = input("Enter an English sentence: ")
    num_consonent, num_vowels = 0, 0
    consonent = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(x)):
        if x[i] in string.ascii_letters:
            if x[i] in consonent:
                num_consonent += 1
            else:
                num_vowels += 1

    print(num_consonent)
    print(num_vowels)


# 12
def leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or (year % 4 == 0 and year % 400 == 0):
        print("It's a leap year")
    else:
        print("It's not a leap year")


# 14
def phonecard():
    x = int(input("Please enter the amount you want on card: "))
    if x == 5 or x == 10:
        return x

    if x == 25:
        return x + 3

    if x == 50:
        return x + 8
    if x == 100:
        return x + 20

    else:
        print("You can not charge in this value.")


# 19
def date_time():
    x = input("Please enter the stores date and time: ")
    t = x.split(' ')
    year = t[0].split('/')
    month = year[0]
    day = year[1]
    year_ = year[2]
    time = t[1].split(':')
    hour = time[0]
    minutes = time[1]
    seconds = time[2]
    if int(month.lstrip('0')) > 12 or int(day.lstrip('0')) > 31 or len(year_) > 4:
        print("invalid date!")

    if int(hour.lstrip('0')) >= 24 or int(minutes.lstrip('0')) >= 60 or int(seconds.lstrip('0')) >= 60:
        print("invalid time!")

    else:
        print(day + '/' + month + '/' + year_)
        print(hour + ':' + minutes + ':' + seconds)
        print(month + '/' + year_)
        if int(hour.lstrip('0')) >= 12:
            print("PM")
        else:
            print("AM")


# 27
import re


def hapaxname(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read().lower())
    frequency = {key: 0 for key in words}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word in frequency:
        if frequency[word] == 1:
            print(word)


# 11
def safe_input(prompt, type_element):
    if (type_element not in (str, int, float)):
        raise ValueError("Expected str, int or float")

    while True:
        test = input(prompt)
        try:
            result = type_element(test)
        except ValueError:
            print("Invalid type, enter again")
        else:
            break

    return result


# 12
def prompt_open(mode):
    while True:
        filename = input("Enter the file name to open")
        try:
            handlefile = open(filename, mode)
            return handlefile
        except IOError:
            print("File name doesn't exist")


#51
def findmin(list_of_values):
    min_val = list_of_values[0]
    for i in range(len(list_of_values)):
        if list_of_values[i] < list_of_values[i - 1]:
            min_val = list_of_values[i]

    print(min_val)


def findmax(list_of_values):
    max_val = list_of_values[0]
    for i in range(len(list_of_values)):
        if list_of_values[i] > list_of_values[i - 1]:
            max_val = list_of_values[i]
    print(max_val)

#52
def gettysburg(address):
    getty = address.split()
    res = []
    i = 0
    while i < len(getty):
        res += [(getty[i], getty[i + 1])]
        i += 2
    print(res)


#57
#(a)
def findhole(lowerstring):
    holeletter = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    count, uncount = 0, 0
    for i in range(len(lowerstring)):
        if lowerstring[i] in holeletter:
            count += 1
        else:
            uncount += 1
    #with holes
    print(count)
    #without holes
    print(uncount)

#(b)
def findholeword(list_of_words):
    holeletter = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    count = 0
    word_list = []
    for word in list_of_words:
        for c in word:
            if c in holeletter:
                count += 1
        if count >= 2:
            word_list.append(word)
            count = 0

    print(word_list)

#(c)
def findholedword(list_of_words):
    holeletter = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q', 'A', 'B', 'D', 'O', 'P', 'Q', 'R']
    count = 0
    word_list = []
    for word in list_of_words:
        for c in word:
            if c in holeletter:
                count += 1
        if count >= 2:
            word_list.append(word)
            count = 0

    print(word_list)


