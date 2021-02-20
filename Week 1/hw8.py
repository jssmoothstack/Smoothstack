#1
def func():
    print("Hello World")

func()

#2
def func1(name):
    print("Hi my name is " + name)

func1("Google")

#3
def func3(x,y,z):
     return x if z else y

print(func3('hello', 'goodbye', False))

#4
def func4(x,y):
    return x*y

print(func4(11,13))

#5
def is_even(num):
    return True if num % 2 == 0 else False

print(is_even(7))

#6
def is_bigger(x,y):
    return True if x > y else False

print(is_bigger(7,5))

#7
def adder(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(adder(6,9,3,1))

#8

def even_list(*args):
    evens = []
    for arg in args:
        if arg % 2 == 0:
            evens.append(arg)
    return evens

print(even_list(3,4,5,7,8))

#9
def case_changer(phrase):
    ans = ''
    return ans.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(phrase))

print(case_changer("potato"))

#10
def parity_check(a,b):
    return min(a-1, b-1) if a % 2 == 0 and b % 2 == 0 else max(a+1, b+1)

print(parity_check(6,8))
        

#11
def starts_with(string1, string2):
    return True if string1[0].lower() == string2[0].lower() else False

print(starts_with("cat", "Carrot"))

#12
def num_squared(*args):
    ans = []
    for arg in args:
        ans.append(arg ** 2)
    return ans

print(num_squared(4,7,317))

#13
def one_four(string1):
    ans = ''
    position = [0,3]
    return ans.join(char.upper() if i in position else char for i, char in enumerate(string1))

print(one_four("burger"))