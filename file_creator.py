name = input("What's your name? \n")
color = input("What is your favorite color? \n")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file \n")
    file.write(f"{color} is user's favorite color \n")