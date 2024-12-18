# 19. Python Password Generator

import random
print("Welcome To The Python Password Generator")

Letters = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

print("Welcome To The Python Password Generator!")
No_Letters = int(input("How Many Letters Would You Like In Your Password?\n:- "))
No_Numbers = int(input("How Many Symbols Would You Like In Your Password?\n:- "))
No_Symbols = int(input("How Many Numbers Would You Like In Your Password?\n:- "))


Password = ""
for char in range(1, No_Letters + 1):
    Password += random.choice(Letters)

for chai in range(0, No_Numbers):
    Password += random.choice(Numbers)

for chai in range(0, No_Symbols):
    Password += random.choice(Symbols)

print(Password)
