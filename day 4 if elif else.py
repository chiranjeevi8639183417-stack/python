"""# ifnd whether the number is +ve even, _ve even, +ve odd, -ve odd,

n=10
if(n%2==0 and n<0):
    print( "n is +ve even number")
elif(n%2==0 and n>0):
    print("n is  -ve even number")
elif(n%2!=0 and n<0):
    print("n is +ve odd numeber")
elif(n%2!=0 and n>0):
    print("n is -ve odd number")
else:
    print(" invalid number")"""

# find the biggest number amoung the three numbers .->#same problem in nested if statement.
n1=int(input())
n2=int(input())
n3=int(input())
if (n1>n2)and(n1>n3):
    print("n1 is big")
elif(n2>n3):
    print("n2 is big")
else:
    print("n3 is big")
          

# Program to find the biggest number among three using nested if"""

a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if a >= c:
        print("The biggest number is:", a)
    else:
        print("The biggest number is:", c)
else:
    if b >= c:
        print("The biggest number is:", b)
    else:
        print("The biggest number is:", c)
"""# Check for Boolean
value = input("Enter something: ")
if value.lower() == "true":
    print("Boolean: True")
elif value.lower() == "false":
    print("Boolean: False")

# Check for Integer
elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
    print("Integer")

# Otherwise it's a String
else:
    print("String")"""

   

        

        
