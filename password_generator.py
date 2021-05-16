import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!$,.(')"

while 1:
    password_length = 15
    password_count = int(input("Enter how many passwords you would like: "))
    
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_char = random.choice(chars)
            password      = password + password_char
    print("Your password is: ",password)
    break
    

