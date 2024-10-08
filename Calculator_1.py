print("*"*100)
print("\t\t\t\t*-----CALCULATOR APP-----*")
print("*"*100)
while (True):
    print("-"*50)
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Mod Division")
    print("6. Exponentiation")
    print("7. Exit")
    print("-"*50)
    choice=int(input("Enter Your Choice:"))
    match(choice):
        case 1:
            print("Enter Two Values for Addition")
            a,b=float(input()),float(input())
            print("Sum({},{})={}".format(a,b,a+b))
        case 2:
            print("Enter Two Values for Substraction")
            a,b=float(input()),float(input())
            print("Sub({},{})={}".format(a,b,a-b))
        case 3:
            print("Enter Two Values for Multiplication")
            a,b=float(input()),float(input())
            print("Mul({},{})={}".format(a,b,a*b))
        case 4:
            print("Enter Two Values for Division")
            a,b=float(input()),float(input())
            print("Normal Div({},{})={}".format(a,b,a/b))
            print("Floor Div({},{})={}".format(a,b,a//b))
        case 5:
            print("Enter Two Values for Mod Division")
            a,b=float(input()),float(input())
            print("Mod Div({},{})={}".format(a,b,a%b))
        case 6:
            a,b=float(input("Enter Base:")),float(input("Enter Exp:"))
            print("Power({},{})={}".format(a,b,a**b))
        case 7:
            print("Exit...")
            break
        case _:
            print("Your Selection Of Operation Is Wrong---Try Again")
    print("Execution Completed!!!...")