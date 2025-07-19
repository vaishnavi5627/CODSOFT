while True:
    print("______________________")
    print("______________________")
    print("1.ADDITON")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.EXIT")
    print("______________________")
    
    choice = input("Enter your choice:")

    if choice == '5':
        break

    a = float(input("Enter 1st number:"))
    b = float(input("Enter 2nd number:"))

    if choice == "1":
        print(a, "+", b, "=", (a+b))

    elif choice =="2":
        print(a, "-", b, "=", (a-b))

    elif choice =="3":
        print(a, "*", b, "=", (a*b))

    elif choice=="4":
        if b == 0.0:
            print("Error! NOt divided by zero")    
        else:
            print(a, "/", b, "=", (a/b))
    else:
        print("Invalid choice")

    print()                        