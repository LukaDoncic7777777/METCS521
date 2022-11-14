#1
from curses.ascii import isdigit
from re import I


def divisible():
    count = 0
    for i in range(100, 999):
        if i % 17 == 0:
            count += 1

    return count

#5
#(a)4， 2， 3， 11
#(b)assignment1: (my_var != 2 && my_var % 2 == 0). 
#   assignment2: (my_var == 2)
#   assingment3: (my_var % 2 != 0 && my_var <= 10)
#   assignment4: (my_var % 2 != 0 && my_var > 10)

#6
def print_alpha(c):
    for i in range(len(c)):
        a = c[2]
        b = c[5]
        e = c[8]
        d = c[11]
        output = a + b + e + d
    print(output)

print_alpha('alphebetical')
#7
#Statement 1 is True, statement 2 is False

#12
def count():
    odd_num = 0
    even_num = 0
    count_square = 0
    for i in range(2, 26):
        if i % 2 != 0:
            odd_num += 1
        if i % 2 == 0:
            even_num += 1
        if i * i < 26:
            count_square += 1
    print(odd_num)
    print(even_num)
    print(count_square)


count()

#18
#(a)
def consecutive():
    consetive_sum = 0
    X = int(input("Enter Number: "))
    for i in range(1, X + 1):
        consetive_sum += i
    return consetive_sum

print(consecutive())

#(b)
def consecutive_add():
    consecutive_sum = 0
    X = int(input("Enter Number: "))
    for i in range(1, X + 1):
        consecutive_sum += i
        print(consecutive_sum)

consecutive_add()

#(c)
def consecutive_divide():
    consecutive_sum = 0
    X = int(input("Enter Number: "))
    for i in range(1, X + 1):
        consecutive_sum += i
        if (consecutive_sum % i == 0):
            print(consecutive_sum)

consecutive_divide()

#20
def check_str():
    s = input("Input an integer: ")
    while s:
        if not s.isdigit():
            s = input("Error: try again. Input an integer: ")
        else:
            print(f"The integer is: {s}")
            break

check_str()


#22
from math import sqrt
flag = 0
def check_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
    else:
        return False

print(check_prime(4))

#29
def prime_checker():
    counter = 0
    x = int(input("Enter an integer greater than 2: "))
    while x >= 2:
        counter += 1
        print(f"{counter}: {round(sqrt(x), 3)}")
        x = sqrt(x)
        if x < 2:
            break

prime_checker()

#38
def addsum(m):
    res = 0
    while m:
        res += m % 10
        m //= 10
    if res > 9:
        return addsum(res)
    return res

print(addsum(998))
                
    

                