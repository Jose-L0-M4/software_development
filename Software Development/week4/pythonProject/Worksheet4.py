#CONSTANTS:
#RATE_S = 0.20
#RATE_M = 0.23
#ALLOWANCE_1 = 2500
#ALLOWANCE_2 = 2000

#USER INPUTS:
#marital_status = input("what is your marital status type 's' for single and 'm' for marry : ")
#emp_id = input(" enter your employee identification :")
#name = input("enter your name: ")
#address = input("Enter Your address")
#gross_pay = input("enter your gross pay")

#ASSIGN ALLOWANCE:
#if gross_pay < 50000;
#  allowance = ALLOWANCE_1
#else:
#   allowance = ALLOWANCE_2

#CALCULATE TAX:
#if marital_status == "s" or "S":
#    total_tax = (gross_pay - allowance) * RATE_S
#elif marital_status == "m" or "M":
#  total_tax = (gross_pay - allowance) * RATE_M
#else:
#  print("Enter a real value")

#CALCULATE NET PAY
#net_pay = gross_pay - total_tax

#OUTPUTS
#emp_id
#name
#address
#marital_statues
#gross_pay, total_tax, net_pay


#BEGIN

#CONSTANTS:
RATE_S = 0.20
RATE_M = 0.23
ALLOWANCE_1 = 2500
ALLOWANCE_2 = 2000

#USER INPUTS:
marital_status = input("What is your marital status type 's' for single and 'm' for marry: ")
emp_id = input(" Enter your employee identification: ")
name = input("Enter your name: ")
address = input("Enter Your address: ")
gross_pay = int(input("Enter your gross pay: "))

#ASSIGN ALLOWANCE:
if gross_pay < 50000:
    allowance = ALLOWANCE_1

else:
    allowance = ALLOWANCE_2

#CALCULATE TAX:
if marital_status == "s" or "S":
    total_tax = (gross_pay - allowance) * RATE_S


elif marital_status == "m" or "M":
    total_tax = (gross_pay - allowance) * RATE_M

else:
    print("Enter a real value please")


#CALCULATE NET PAY
net_pay = gross_pay - total_tax


#PASSWORD STORED:
password = input("Ingress a password to increase security: ")

#match password
re_enter_password = input("Ingress password to verify and see information: ")
if password == re_enter_password or len(password) == 0:
    print("Your employee identification is:\t" + emp_id)
    print("Your name is:\t" + name)
    print("Your address is:\t" + address)
    print("Your marital status is:\t" + marital_status)
    print("Your gross pay is:\t" + str(gross_pay))
    print("Your total tax is:\t" + str(total_tax))
    print("Your net pay is:\t" + str(net_pay))

else:
    print("ACCESS DENIED")










