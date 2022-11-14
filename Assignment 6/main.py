from matplotlib import pyplot as plt

# 22
def convert_list(listA):
    listB = []
    listB.append(listA[0] + listA[1])
    i = 1
    while i < len(listA) - 1:
        listB.append(listA[i - 1] + listA[i] + listA[i + 1])
        i += 1
    listB.append(listA[i - 1] + listA[i])
    print(listB)


import string


# 24
# (a)
def convert_words():
    X = input("Enter a string: ")
    list_of_words = X.split(" ")
    listA = []
    i = 0
    while i < len(list_of_words):
        newS = list_of_words[i].translate(str.maketrans('', '', string.punctuation))
        listA.append(newS)
        i += 1
    print(listA)


#(b)
def convert_word():
    X = input("Enter a string: ")
    listA = []
    for ele in X:
        if ele in string.punctuation:
            X = X.replace(ele, "")

    new_Str = X.split(" ")
    listA.append(new_Str)
    print(listA)

# 39
# (a)
def convert_integer(L):
    new_list = [x for x in L if x % 2 == 0]
    print(sum(new_list))



# (b)
def convert_odd(L):
    new_list = [x for x in L if x % 2 != 0]
    print(sum(new_list))


# 52
def gettysburg(address):
    getty = address.split()
    res = []
    i = 0
    while i < len(getty):
        res += [(getty[i], getty[i + 1])]
        i += 2
    print(res)


# 63
def combine_number(listA):
    word = [str(num) for num in listA]
    print("".join(word))


# 6
def createzip(listA, listB):
    dictionary = dict(zip(listA, listB))
    print(dictionary)


# 8
# (a)
def printkey(my_dict):
    print(list(my_dict.keys()))


# (b)
def printvalue(my_dict):
    print(list(my_dict.values()))


# (c)
def printpair(my_dict):
    for key, value in my_dict.items():
        print(key, value)


# (d)
def order_key(my_dict):
    for i in sorted(my_dict):
        print((i, my_dict[i]))


# (e)
def order_value(my_dict):
    print(sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0])))


# 14
# (a)
def convert_string():
    X = input("input a string: ")
    X = X.strip()
    max_frequency = {}
    for i in X:
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1
        my_result = max(max_frequency, key=max_frequency.get)
    print(my_result)


# (b)
def convert_dict():
    X = input("Input a string: ")
    X = X.strip()
    letter_dict = {}
    for i in X:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    print(letter_dict)


# (c)
def convert_his():
    X = input("Input a string: ")
    X = X.strip()
    letter_dict = {}
    for i in X:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    plt.bar([x for x in letter_dict.keys()], letter_dict.values(), 2, edgecolor=(0, 0, 0))
    plt.axis([-5, 105, 0, 5])

    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("letter")
    plt.ylabel("Number of occurence")
    plt.title("Distribution of occurrence")
    plt.show()


# 19
def create_month():
    dict = {'January': 31, 'February': '28', 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'Jury': 31, 'August': 30,
            'September': 31, 'October': 30, 'November': 31, 'December': 30}
    print(dict)


# 26
def prompt_number():
    X = input("Enter number: ")
    dict = {'1': 'One', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
            '9': 'nine', '0': 'zero'}
    empty = []
    for i in X:
        empty.append(dict[i])

    print(" ".join(empty))

