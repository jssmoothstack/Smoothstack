import math

# Question 1

print((50+50) + (100-10)) # 190

# Question 2

# 30 + *6 will result in a syntax error
print(6^6) # XOR operator, performs bitwise on each input in binary
print(6**6) # 36
print(6+6+6+6+6+6) # 36

# Question 3

print("Hello World")
print("Hello World : 10")

# Question 4

def payment_calculator(P, R, L):
    rate = R / 12
    numerator = rate * ((1 + rate) ** L)
    denominator = ((1 + rate) ** L) - 1

    return math.ceil((P * numerator) / denominator)

print(payment_calculator(800000, .06, 103))