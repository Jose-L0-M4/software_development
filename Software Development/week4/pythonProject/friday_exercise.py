#CONSTANTS
HOURLY_WAGE = 12.25
TIME_BONUS = 0.5
SALES_VOLUMES = 50.00
COMMISSION = 5 / 100
BONUS = 38

#INPUTS
hours_worked = float(input("Enter your hours worked : "))
commission = float(input("What is your sales volume: "))
bonus = 0

#CONDITIONAL HOURS WORKED:
if hours_worked > BONUS:
    bonus = hours_worked - BONUS
    total = (hours_worked * HOURLY_WAGE) + ((hours_worked - BONUS) * (HOURLY_WAGE * TIME_BONUS))

else:
    total = hours_worked * HOURLY_WAGE

#CONDITIONAL COMMISSION EARNED
if commission > 50:
    total_2 = commission * COMMISSION

else:
    total_2 = 0

#CALCULATION
total_3 = total + total_2


#OUTPUTS
print("Your hours worked are: ",hours_worked)
print("Bonus hours are :",bonus)
print("You earned :",total)
print("Your commission is :",total_2)
print("Your total earned :",total_3)


#Question 2

euro = int(input("Enter a value of cents: "))

change = euro/100

print("this is how much you have in euro :",change)

PURCHASE_PRICE = 35.8

if change > PURCHASE_PRICE:
    print(" You can buy this")
    change_2 = change - PURCHASE_PRICE

    str(change_2)
    print(change_2[0])
    print(change_2[1])



else:
    print("You can't buy this")







