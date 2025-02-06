#Exercise 1

import time

date = input("Enter your date of birth in the next format dd/mm/yyyy:")

year = time.strftime("%Y")

user_y = int(date[6:])

age = int(year) - user_y

print("You are",age,"old, haha you're a boomer")

#Exercise 2

import math

PI = math.pi

area = int(input("Enter area of your circle"))

radius = math.isqrt(int(area/(PI * 2 )))

print(radius)



#exercise 3

name = input("whats your name lit bro: ")
surname = input("Now your surname my darling: ")

print("thanks for share your full name "+name.capitalize(),surname.capitalize())

#exercise 4
import random

magic_num = random.randint(1,5)

print("your magic number is :",magic_num)

counter = 1
total = 0
product = 1
while counter < magic_num:
    total += counter
    product *= 1
    counter += 1

print("the sum of the numbers from",1, "to" , magic_num, "is equal to",total)
print("the product of the numbers from",1, "to" , magic_num, "is equal to",product)


#exercise 5

counter = 1
while counter < 21:
    if counter % 2 == 0:
        print(counter,"even")

    else:
        print(counter,"odd")

    counter += 1


#Exercise 6

print("Put 3 words to create a acronym")

word_1 = input("First word :")
word_2 = input("Second word :")
word_3 = input("Third word :")

Acronyms = word_1[0].upper()+word_2[0].upper()+word_3[0].upper()

print(Acronyms)





