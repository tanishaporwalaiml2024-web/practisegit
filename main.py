while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Divide")
    print("4.Multiply")
    print("5.Modulus")
    print("6.Floor Division")
    print("7.Power")
    print("0.End")

    n=input("Enter your choice: ")
    if n==0:
        print("Exit")
        break

    a=float(input("Enter number: "))
    b=float(input("Enter number: "))

    if n==0:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a/b)
    elif n==4:
        print(a*b)
    elif n==5:
        print(a%b)
    elif n==6:
        print(a//b)
    elif n==7:
        print(a**b)
    else:
        print("Invalid choice...")