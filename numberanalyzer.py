def oddeven(n):
    if n %2==0:
        print("Even numbers")
    else:
        print("Odd numbers")
n=int(input("Enter a number:"))
oddeven(n)       

def checksign(num):
    if num>0:
        print("Positive number")
    elif num<0:
        print("Negative number") 
    else:
        print("Zero")
n=int(input("Enter a number:" ))
checksign(n)       

def square(num):
    print("Square=",num*num)
n=int(input("Enter a number:"))    
square(n)

