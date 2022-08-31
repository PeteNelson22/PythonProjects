def add(a,b):
    print('Addition =',a + b)

def sub(a,b):
    print('Subtraction =', a - b)

def mult(a,b):
    print('Multiplication =', a * b)

def div(a,b):
    print('Division =', a / b)

def mod(a,b):
    print('Modulus =', a % b)

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exit")

    ch = int(input("Enter your choice "))

    if ch==1:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        add(a,b)
    
    elif ch==2:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        sub(a,b)

    elif ch==3:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        mult(a,b)

    elif ch==4:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        div(a,b)
    
    elif ch==5:
        a = int(input("Enter first number "))
        b = int(input("Enter second number "))
        mod(a,b)

    elif ch==6:
        break

    else:
        print("Wrong choice")