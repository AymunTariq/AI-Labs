import numpy as np
import math as m


def factorial (data):
    return m.factorial(data)


def askNumber():
    num1 = input("Enter first Number: ")
    num2 = input("Enter second Number: ")
    return int(num1), int(num2)


def add(num1, num2):
    return num1 + num2


def mul(num1, num2):
    return num1 * num2


def Menu():
    return input("Press the Operation to want: ")


def main():
    operator = Menu()
    if (operator == "+"):
        num1, num2 = askNumber()
        return add(num1,num2)
    elif(operator == "*"):
        num1, num2 = askNumber()
        return mul(num1,num2)
    else:
        print("Sorry Software does not support the operator.")
        return -1


def fib (n):
    list =[0, 1]
    for i in range(n-1):
        fibn1 = list[-2]
        fibn2 = list[-1]
        list.append(fibn1 + fibn2)
    return list



def ToPigLatin(english):
    wordlist = english.split()
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(wordlist)):
        if (wordlist[i][0] in vowels):
            wordlist[i] = wordlist[i] + 'hay'
        else:
            wordlist[i] = wordlist[i][1:] + wordlist[i][0] + 'ay'
    return wordlist


# data = input("Enter number for Factorial: ")
# print("Factorial is: ", factorial(int(data)))
#
# interrupt = 1
# while (interrupt):
#     calculated_Res = main()
#     print("Your answer is: ", calculated_Res)
#     interrupt = input("Want to quit? enter 0, else enter 1")
#     interrupt = int(interrupt)

# data = input("enter number for Fibonacci: ")
# print(fib(int(data)))

# english = input("Write some english dude: ")
# print(
# ToPigLatin(english))