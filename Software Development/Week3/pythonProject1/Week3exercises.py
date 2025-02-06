#Exercise 1

hours = int(input("give me your time for hours part :"))
secs = int(input("give me your time in second part :"))
mins = int(input("give me your time in minutes part :"))

SECS_PER_HOURS = 360
SECS_PER_MIN = 60

SECS_PER_MIN = mins * SECS_PER_MIN
SECS_PER_HOURS = hours * SECS_PER_HOURS


total = secs + SECS_PER_HOURS + SECS_PER_MIN

print("Your seconds in hours are",str(SECS_PER_HOURS))
print("Your minutes in seconds  are",str(SECS_PER_MIN))
print("Your seconds in seconds are",str(hours))
print("Your hours in addition with minutes and second are",str(total))

#Exercise 2

radius = int(input("tell me the radius to find the area :"))

PI = 3.14159

area = PI * radius**2

print("The area of this circle is "+ str(round(area,3)), end="\n")

#Exercise 3

word_1 = input("give me your First word :")
word_2 = input("give me your Second word :")
word_3 = input("give me your Third word :")

acronym = word_1[0] + word_2[0] + word_3[0]

print("you 3 words was",word_1, word_2, word_3, "the acronym is :",acronym.upper())

#Exercise 4

password = input("add password :")
space_loc = password.index("!")
print(type(space_loc))
print("the lenght of our password is",len(password))
print("! is found in "+ str(space_loc) +" place.")

#Exercise 5
print("give 4 characters or more :",end="")
word = input()

two_characters = word[0:2]

print("this is what you wrote :",word)
print("this is what the program made :",two_characters)

#exercise 6

user_word = input("write a word :")
number = int(input("how many times you want to multiply this :"))

concatenation = (user_word + " ") * (number - 1) + user_word

print("Your original word is "+ user_word)
print("The newly created string is \""+concatenation+"\"", end="")

#Exercise 7

EXTENSION = ".py"
file = input("\nname of your file")
concatenation = file + EXTENSION

print("your file name is :",concatenation)

#Exercise 8

time = int(input("give me your time in seconds :"))

SECS_PER_HOURS = 360
SECS_PER_MIN = 60

SECS_PER_MIN = time / SECS_PER_MIN
SECS_PER_HOURS = time / SECS_PER_HOURS

HOURS = time


print("Your second in hours are",str(round(SECS_PER_HOURS,2)))
print("Your seconds in minutes are",str(round(SECS_PER_MIN, 2)))
print("Your seconds in seconds are",str(time))
