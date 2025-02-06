import random
import time

print("*"*24)
print("*"+(" "*6)+"Gym System"+ (" "*6) + "*")
print("*"*24)
print("1. Register")
print("2. Statistics")
print("3. Generate Member's ID")
print("4. Exit")
print("*"*24)


counter = 0

option = int(input("Option:"))

while option != 4:

    # option 1
    if option == 1:
        name = input("Name: ")
        year = int(input("Year born:"))
        fees = round(2000,2)
        actual_year = int(time.strftime("%Y"))
        while year > 2008:
            year = int(input("Re-enter Year born:"))

        age = actual_year - year
        if age >= 60:
            discount = 1000
            percentage = "50%"

        elif age >= 50 and age <60 :
            discount = 500
            percentage = "25%"

        else:
            discount = 0
            percentage = "0%"

        payment = fees - discount
        print("Member: "+name)
        print("Age :"+str(age))
        print("Fees Due:", fees)
        print("percentage Fees discount:"+percentage)
        print("Amount Fees discounted", ":" + "€" + str(discount))
        print("Amount Fees to be paid",":" + "€" + str(payment))
        counter += 1

    #option 2
    elif option == 2:
        print("*" * 30)
        print("*" + (" " * 6) + "Daily statistics" + (" " * 6) + "*")
        print("*" * 30)
        print("Number Registered:", counter)
        print("Total Fees Due  :"+ str(float(payment)))
        print("Total Discount given  :" + str(float(discount)))


     #option 3
    elif option == 3:
        actual_year = time.strftime("%Y")

        member_id = "Max Gym"+actual_year

        member_id_2 = ""

        for character in member_id:
            if " " in character:
                character = ""
            member_id_2 += character
        print(member_id_2)
        new = ""
        number = random.randint(1,99)
        for character in member_id_2:
            if (member_id_2.index(character)+1) % 2 == 0:
                new += character
            else:
                new += ""

        print(new+str(number))



    else:
        option = int(input("Pick a real option:"))



    option = int(input("Option:"))

print("Bye")