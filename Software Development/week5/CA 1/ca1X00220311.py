#Jose Lo Mantilla
#X00220311


#CONSTANTS
HAT = 10
CHARACTER = 2.00

#INPUT
message = input("Enter message :")

quantity = int(input("Enter quantity :"))

sign_up = input("Enter a valid email :")

cost_hat = quantity * HAT

cost_character = len(message) * CHARACTER

total = cost_hat + cost_character

discount = total * (10/100)


#OUTPUT

if quantity >= 5 :
    total_2 = total - round(discount,3)
    print("This is the discount :",round(discount,3))
    print("the quantity ordered are: " + str(quantity) + " and the cost is:", total_2)


else:
    print("the quantity ordered are: " + str(quantity) +" and the total cost (character + hat) is:", total)




print("The character you want to print are",len(message))
print("The cost of the hat is:",cost_hat)



if "@" in sign_up:

    if sign_up.index("@") >= 3 and sign_up.index("@") >= -3:

        password = sign_up[sign_up.index("@") - 3 :sign_up.index("@")] + sign_up[sign_up.index("@")+1:sign_up.index("@") + 3]

        if len(sign_up) % 4 == 0:
            password = password + str(400)
            print("your password is :" + password)
            print("your email is :" + sign_up)

        else:
            password = password + str(300)
            print("your email is :" + sign_up)
            print("your password is :" + password)

    else:
        print("add more words")

else:
    print("don't contain \"@\"")










