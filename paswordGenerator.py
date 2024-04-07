

import random
import string

alpha = list(string.ascii_letters)
num = list(string.digits)
symbol = list(string.punctuation)

letter = int(input("Enter how many letter you want to in your password: "))
digit  = int(input("Enter how many number you want to in your password: "))
symb   = int(input("Enter how many symbol you want to in your password: "))

password=''

for i in range(letter):
    a = random.choice(alpha)
    password+=a

for j in range(digit):
    b = random.choice(num)
    password+=b
    
for k in range(symb):
    c = random.choice(symbol)
    password += c
    
print(password)
