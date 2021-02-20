#1
def div_seven(a, b):
    ans = []
    for num in range(a, b+1):
        if num % 7 == 0 and num % 5 != 0:
            ans.append(num)
    return ans

print(div_seven(1500, 2700))

#2
def temp_convert(num):
    fahrenheit = round((num * (9/5) + 32), 1)
    celsius = round((num - 32) * (5/9), 1)
    return str(num) + " degrees Celsius is " + str(fahrenheit) + " degrees Fahrenheit. " + str(num) + " degrees Fahrenheit is " + str(celsius) + " degrees Celsius."

print(temp_convert(60))

#3
import random

def num_guesser():
    correct = random.randint(1,9)
    guess = 0

    while guess != correct:
        guess = input("Guess a number between 1 and 9 inclusive: ")
        if int(guess) == correct:
            return print("That was the correct number!")
        else:
            print("That guess was incorrect, please try again.")

num_guesser()

#4
def stars():
    for i in range(1, 6):
        print("*" * i)
        #print("\n")
        if i == 5:
            for j in range(4, 0, -1):
                print("*" * j)
                #print("\n")

stars() 


#6
def reverser(word):
    return word[::-1]

print(reverser("wyvern"))

#7
def parity_count(*args):
    evens, odds = 0, 0
    for arg in args:
        if arg % 2 == 0:
            evens += 1
        else:
            odds += 1
    return "Number of even numbers: " + str(evens) + "\n" + "Number of odd numbers: " + str(odds) + "\n"

print(parity_count(1,3,5,8))

#8
def type_finder(*args):
    for arg in args:
        print(str(arg) + ": " + str(type(arg)) + "\n")

type_finder("dog", 8, (9,1), [0])

#9
def numbers():
    i = 0
    while i < 7:
        if i == 3 or i == 6:
            i += 1
            continue
        print(str(i) + " ")
        i += 1

numbers()