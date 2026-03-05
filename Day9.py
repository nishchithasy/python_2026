#Decision making (conditional statements)
#if else statements are used to checking the conditions
x =10
if x == 10:
    print("Yes value of x is 10")
else:
    print("No value of x is not 10")

a = int(input("Enter a number, a= "))
if a%2!=0:
    print("Not an even")
elif a%2==0:
     print("An even number")
else:
    print("Enter only numbers")

att=int(input("\nEnter your current attendence percentage: "))
if att>=75:
    print("Your are not in the attendance shortage list")
    print("***Congrats***")
else:
    print("You have to pay the fine!!!")