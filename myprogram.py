print("Hello text")
print(7)
greeting = "Hello"
print(greeting)

# greeting2 = input("Write a greeting: ")
# print(greeting2)

a = 2
b = 3

print(a + b)
print(type(2))

# age = input("Enter your age: ")
# new_age = int(age) + 50
# print(new_age)

print(3**2)

newgret = greeting.replace("e", "i")
newgret = greeting.replace("e", "i", 1)
print(newgret)

# print(dir(newgret))

print(newgret[0])
print(newgret[-1])
print(newgret[0:3])
print(newgret[:4])
print(newgret[3:])

# List mutable
c = ["H", 2, "Hello"]
print(c)
print(type(c[1]))
c.append(4)
print(c)
c.remove("H")
print(c)

# Tuple not mutable
t = ("Hello", 2 , 4.6)
print(t)

# Dictionary unordered
d = {"Name" : "John", "Surname" : "Smith", "Cities": ("Porto", "San diego", "Bali")}
print(d)
print(d["Name"])
print(d["Cities"][1])

def minutes_to_hours(seconds, minutes=70):
    hours = (minutes / 60.0) + (seconds / 3600)
    return hours

print(minutes_to_hours(300))

# def age_foo(age):
#     new_age = float(age) + 50
#     return new_age

# age = input("Enter your age: ")

# if age < 150:
#     print(age_foo(age))
# else:
#     print("How it is possible?")

a = 5

if a < 5:
    print("less than 5")
elif a == 5:
    print("equal to 5")
else:
    print("equal or greater than 5")

emails = ['me@gmail.com', 'you@gmail.com', 'them@mail.com']
for email in emails:
    if 'gmail' in email:
        print(email)

# def currency_converter(rate, euros):
#     dollars = euros * rate
#     return dollars
# r = input("Enter rate: ")
# e = input("Enter euros: ")
# print(currency_converter(r, e))

# password = ""
# while password != "python123":
#     password = input("Enter password: ")
#     if password == 'python123':
#         print("You are logged in!")
#     else:
#         print("Sorry, try again!")

names=['james', 'john', 'jack']
email_domains=['gmail', 'yahoo']

for i,j in zip(names, email_domains):
    print(i, j)

file = open("example.txt", "r")
content = file.read()
print(content)
file.seek(0)
content2 = file.readlines()
print(content2)

content2 = [i.rstrip("\n") for i in content2]
print(content2)

file = open("example.txt", "w")
file.write("Line 1\n")
file.write("Line 2\n")

for i in range(10):
    file.write("Line " + str(i) + "\n")

file = open("example.txt", "a")
file.write("Line 11\n")
file.close()

with open("example.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)

import os
print(os.listdir("."))
print(os.__file__)

"""
This script creates an empty file
"""
def create_file():
    """
    This function creates an empty file
    """
    with open("example.txt", "w") as file:
        file.write("")

import datetime
print(datetime.datetime.now())
print(datetime.datetime(2016, 5, 13, 11))
print((datetime.datetime.now() - datetime.datetime(2016, 5, 13, 11)).days)
print(datetime.datetime.now().strftime("%Y-%m-%d-%H"))
print(datetime.datetime.now()+datetime.timedelta(days=2))

import time
lst = []
for i in range(5):
    lst.append(str(datetime.datetime.now()))
    #time.sleep(1)
print(lst)