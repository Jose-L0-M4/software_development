#Exercise 1

number = 0 + 50

while number <= 100:
    print(number)
    number += 1


for number in range(50,101):
    print(number)


#Exercise 2
adding = 0

for times in range(5):
    number = float(input("enter the value number " + str(times + 1)+":"))
    adding += number

average = adding/5
print("the average is:",average)
print("the sum of all is :",adding)

#Exercise 3
total = 0
total_2 = 0
for number in range(1,21):
    if number % 2 == 0:
        total += number

    else:
        total_2 += number
print("the sum of even numbers between 1 to 20:",total)
print("the sum of odd numbers between 1 to 20:",total_2)
#Exercise 4

EUR_TO_YEN = 165

euro = float(input("Enter your amount of Euros :"))

while euro != 0:
    total = euro * EUR_TO_YEN
    print("This what You have in Yen currency: " + str(total))
    euro = float(input("Enter your amount of Euros :"))




#Exercise 5

start_num = int(input("Enter the start number :"))
end_num = int(input("Enter the end number :"))
step_num = int(input("Enter the steps number :"))

total = 0
for number in range(start_num,end_num,step_num):
    print(number)
    total += number

print("The sum of all these numbers is:",total)








