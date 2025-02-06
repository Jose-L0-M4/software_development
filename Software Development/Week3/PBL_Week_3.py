#Question 1

#inputs
#loan
#annual_interest_rate
#loan_period
#annual_interest_rate/=100


#Processing
#monthly_payment=(loan_amount*rate)/(1-(1/(1+rate))**number_of_payments
#Number_of_payment=loan_period* 12
#rate = annual_interest_rate / 100.0 / 12


#Output
#print(monthly_payment)

loan_amount = float(input("Tell me your loan :"))
annual_interest_rate = float(input("Tell me your annual interest rate :"))
loan_period = float(input("Tell me in how many years this will be pay :"))
annual_interest_rate/=100


rate = annual_interest_rate / 100.0 / 12
Number_of_payment = loan_period * 12

monthly_payment = (loan_amount * rate)/ (1-(1/(1+rate))**Number_of_payment)

print("The result of the calculator is :",monthly_payment)

#Question 2

number_hamburgers = int(input("how many hamburgers you want :"))
number_chips = int(input("how many portions of chips you wish :"))

HAMBURGER_COST = 80/100
HAMBURGER_SALES = 3.5
PORTION_OF_CHIPS_COST = 60/100
PORTION_OF_CHIPS_SALES = 2.0

profit_ham = (number_hamburgers*HAMBURGER_SALES) - (number_hamburgers*HAMBURGER_COST)
profit_potato = (number_chips*PORTION_OF_CHIPS_SALES) - (number_chips*PORTION_OF_CHIPS_COST)

print("The profit for the hamburgers are",profit_ham)
print("The profit for the chips are",profit_potato)

