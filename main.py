import random

symbol = "1234567890-=qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
pass_length = int(input("Какая длина пароля:"))

password = ""
for i in range(pass_length):
    password += random.choice(symbol)

print(password)
