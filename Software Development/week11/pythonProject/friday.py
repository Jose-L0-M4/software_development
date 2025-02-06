print("*"* 8+"Salary System"+"*"* 8)
print("\n"+("*"*30))
NO_EMP = 5
net_p = []
emp = []
bracketA=[]
bracketB=[]
bracketC=[]
bracketD=[]

for person in range(NO_EMP):
    print("Employee",person+1)
    pps = input("PPS Number:")
    gross = float(input(("Gross pay: €")))
    emp.append(pps)

    if gross <= 10000:
      tax = 0
      net = gross - tax
      bracketA.append(tax)


    elif  gross <= 20000:
        tax = gross - (gross*0.3)
        net = gross - tax
        bracketB.append(tax)



    elif  gross <= 50000:
        tax = gross - (gross * 0.35)
        net = gross - tax
        bracketC.append(tax)




    else:
        gross -= 15000
        tax = gross*0.4
        net = (gross + 15000) - tax
        bracketD.append(tax)

    print(pps,"has gross pay of €", gross)
    print("paid tax of €", tax, "and has net pay of €", net)

    net_p.append(net)


print("------------------------------")
print("PPS Number\tNet Pay")
for i in range(len(emp)):
    print(emp[i],"\t","€",net_p[i])

print("------------------------------")
print("Tax paid in each bracket")
print("Bracket A\t\t€",sum(bracketA))
print("Bracket B\t\t€",sum(bracketB))
print("Bracket C\t\t€",sum(bracketC))
print("Bracket D\t\t€",sum(bracketD))

print("------------------------------")
print("Number in each bracket")
print("Bracket A\t\t",len(bracketA))
print("Bracket B\t\t",len(bracketB))
print("Bracket C\t\t",len(bracketC))
print("Bracket D\t\t",len(bracketD))





