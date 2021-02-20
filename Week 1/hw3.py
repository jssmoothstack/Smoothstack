#Ex 1
print("Hello World"[-3])

#Ex 2
print("thinker"[2:5])

#Ex 3
S = 'Sammy'
print("s[2:] would result in an error because s is not defined (case-sensitive)")

#Ex 4
print(set('Mississippi'))

#Ex 5

def palindrome_checker(n, *args):
    for arg in args:
        cleaned = ''.join(char for char in arg if char.isalnum())
        cleaned = cleaned.lower()
        print('Y ') if cleaned == cleaned[::-1] else print('N ')

palindrome_checker(3, "stars", "raceCar", "pota,to")