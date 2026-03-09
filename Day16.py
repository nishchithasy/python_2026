#Functions in python

def greet(name):
    print(f"Hi! {name} heartily welcome to python course")

greet("NIshchitha")

def marriage():
    print("Ram married seetha")
    
marriage()

def marriage(boy,girl): #parameters
    print(f"{boy} married {girl}") 

marriage("chandan","chandana")      #positional arguments

def marriage(boy,girl="Devathe"):           #if no input for girl name then make it has default
    print(f"{boy} married {girl}")

marriage("chandan") #default value will be added here
marriage("chandan","sneha")

def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

table(2)

def func(num):
    return int((num)*2)

a=func(2)   #answer 4
b=10
c=a+b   #4+10 = 14
print(c)    #14 is the answer here

marriage(boy="Narendra",girl="chandana")    #keyword arguments

l=[1,2,3,4,5]
l.sort(reverse=True)        #keyword arguments
print(l)


#Global and Local variables

def func():
    x="chandana"
    print("Hello world")
    print(y)
    print(x)

y="Darshan"
func()
#y="Darshan"        should be declare with in the block of code

