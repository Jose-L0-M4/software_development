import math

PI = math.pi
'''
Inputs
choice = int(input("Enter an option :"))
length = float(input("Enter lenght :"))
height = float(input("Enter height :"))
radius = float(input("Enter radius :"))
sphere = (4/3)*PI*(radius**3)
cylinder = PI*(radius**2)*height
cube = length**3
'''
#################################################################################
#Question 1
print("*"*50)
print("*Calculation of volume for solid objects*")
print("*"*50)
print("1. Cube  \n2. Cylinder \n3. sphere \n4. Exit\n"+"*"*20)
choice = int(input("option :"))

while choice != 4:
    if choice == 1:
        length = float(input("Enter lenght :"))
        cube = length ** 3
        print("The volume for this cube is:",round(cube,2))

    elif choice == 2:
        radius = float(input("Enter radius of cylinder :"))
        while radius <= 0:
            radius = float(input("Re-enter radius "))

        height = float(input("Enter height of the cylinder:"))
        cylinder = PI * (radius ** 2) * height
        print("The volume for this cylinder is:",round(cylinder,2))


    elif choice == 3:
        radius = float(input("Enter radius of the sphere :"))
        while radius <= 0:
            radius = float(input("Re-enter radius "))
        sphere = (4 / 3) * PI * (radius ** 3)
        print("The volume for this sphere is:", round(sphere,2))

    else:
        print("Invalid menu option chosen")


    print("*" * 50)
    print("*Calculation of volume for solid objects*")
    print("*" * 50)
    print("1. Cube  \n2. Cylinder \n3. sphere \n4. Exit\n" + "*" * 20)
    choice = int(input("option :"))

print("proccessing of volumes completed")


#################################################################################

#Question 2
sentence = input("Enter a sentence: ")
url = ""
for urlsentence in sentence:
    if urlsentence == " ":
        urlsentence ="%20"
        url += urlsentence

    else:
        url += urlsentence

print(url)

#################################################################################



#Question 3
sentece = input("write a sentence: ")
type = input("write a single character: ")
while len(type) >= 2:
    type = input("single character please: ")

counter = 0
sentece = sentece.lower()
type = type.lower()


for letter in sentece:
    if letter == type:
        counter += 1

    else:
        counter += 0

print("times that "+ type +" appear is",counter)






