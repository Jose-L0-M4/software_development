#CONSTANTS
TOFU_B = 3.49
CAJUN_C = 4.59
BUFFALO_W = 3.99
RAINBOW_F = 2.99

RICE_C = 0.79
NO_SALT_F= 0.69
ZUCCHINI = 1.09
BROWN_R = 0.59

CAFE_M = 1.99
CAFE_L = 1.99
ESPRESSO = 2.49
OOLONG_TEA = 0.99

#INPUTS
print("Enter the number for which item you want:")
print("1)\tTofu Burger\t\t€3.49")
print("2)\tCajun Chicken\t\t€4.59")
print("3)\tBuffalo wings\t\t€3.99")
print("4)\tRainbow Fillet\t\t€2.99\n")
entree = int(input())
total_1 = int(input("How many?\t"))


print("Enter the number for which item you want:")
print("1)\tRice cracker\t\t€0.79")
print("2)\tNo-Salt Fries\t\t€0.69 ")
print("3)\tZucchini \t\t€1.09")
print("4)\tBrown Rice\t\t€0.59\n")
side_d = int(input())
total_2 = int(input("How many?\t"))

print("Enter the number for which item you want:")
print("1)\tCafé Mocha\t\t€1.99")
print("2)\tCafé Latte\t\t€1.99")
print("3)\tEspresso\t\t€2.49")
print("4)\tOolong Tea \t\t€0.99\n")
drinks = int(input())
total_3 = int(input("How many?\t"))

#Entree

if entree <= 4 and entree >= 1:
    if entree == 1:
        entree = total_1 * TOFU_B
        food = "Tofu Burger"

    elif entree == 2:
        entree = total_1 * CAJUN_C
        food = "Cajun Chicken"

    elif entree == 3:
        entree = total_1 * BUFFALO_W
        food = "Buffalo Wings"

    else:
        entree = total_1 * RAINBOW_F
        food = "Rainbow Fillet"

else:
    print("pick a number between 1 and 4")

#Side dish

if side_d <= 4 and side_d >= 1:
    if side_d == 1:
        side_d = total_2 * RICE_C
        food_2 = "Rice cracker"

    elif side_d == 2:
        side_d = total_2 * NO_SALT_F
        food_2 = "No-Salt Fries"

    elif side_d == 3:
        side_d = total_2 * ZUCCHINI
        food_2 = "Zucchini"

    else:
        side_d = total_2 * BROWN_R
        food_2 = "Brown Rice "

else:
    print("pick a number between 1 and 4")

#Drinks

if drinks <= 4 and drinks >= 1:
    if drinks== 1:
        drinks = total_3 * CAFE_M
        food_3 = "Café Mocha "

    elif drinks == 2:
        drinks = total_3 * CAFE_L
        food_3 = "Café Latte"

    elif drinks == 3:
        drinks = total_3 * ESPRESSO
        food_3 = "Espresso"

    else:
        drinks = total_3 * OOLONG_TEA
        food_3 = "Oolong Tea"

else:
    print("pick a number between 1 and 4\n")


print("Your Order:")
print("Entree:",total_1,food,"€",entree)
print("Side dish:",total_2,food_2,"€",side_d)
print("Drinks:",total_3,food_3,"€",drinks,"\n")
print("Total bill:\t\t"+"€",(entree + side_d + drinks))



