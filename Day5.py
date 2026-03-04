#Assignment operators
a = 10

a += 10     #add 10 -> a=20
print(a)
a -= 5      #subtract 5 -> 15 because now a is 20 not 10
print(a)
a /= 2      #divide a by 2 -> 7.5 that is 15/2
print(a)
a *= 100    #multiply by 100 ->750 that is 7.5*100
print(a)
a %= 10     #modulus of 10 ->
print(a)


#comparision operators
a = 10 
b = 20

print(a == b)          #no
print(a != b)          #yes 
print(a >= 10)          #yes
print(a <= 9)           #yes
print(a > b)            #no
print(a < b)            #yes


#Logical operators -> and, or, not
a = 100
b = 500

print((a == b) and (a != b))
print((a <= b) or (a >= b))
print((a < b) and (a != b))
print(not (a == b))




#Membership operators -> in ,not in
name = "Raksha"
name2 = "Raksha H S"

print("k" in name)
print("s" in name2)
print(not("r" in name))
print(" H S" in name2)
print(not(" H " in name))

#Bitwise operators   (operations on binary representation of integers)
a = 5                #In binary it is 101
b = 3                #in binary it is 011
print(a & b)        #and
print(a | b)        #or
print(a ^ b)        
print(a << 1)       #lesser than
print(~a)           #not
print(a>>1)         #greater than


num1 = int(input("Enter the first number: ") )
num2 = int(input("Enter the second number: "))
if((num1 > 10) and (num2 > 10)):
    {
        print("Both the numbers are greater than 10.")
    }
elif num1 > 10 or num2 > 10:
    {
        print("One of the two number is greater than 10.")
    }
else:
    print("None of the numbers are greater than 10.")


num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
if(num1 > num2):
    {
        print("a is greater than b.")
    }
elif num1 == num2:
     {
          print("a is equal to b!")
     }
else :
    print("a is not greater than b.")


age = (int(input("Enter your age: ")))
if age >= 18 :
    {
        print("You are an ADULT!!")
    }
elif(age < 18):
        {
            print("You are still MINOR!! ")
        }
else:
     print("You are not an ADULT!!")


string = str(input("Enter the string: "))
if"python" in string:
     {
        print("Yes, this word is in the string!!")
     }
else:
     print("This word is not in the string")