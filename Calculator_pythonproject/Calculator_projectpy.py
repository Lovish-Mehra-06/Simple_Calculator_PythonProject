#This is a Function
def script():
    # Write the code here....
    # ....
    # ....
    print("\nCalculator")
    print("Enter Your First Number")
    n1 = int(input())
    print("Enter Your Second Number")
    n2 = int(input())
    print("press   0 for Addition     1 for Subtraction      2 for Multiplication      3 for Division")
    oper = int(input())
    if oper == 0:
        print(n1 + n2)
    elif oper == 1:
        print(n1 - n2)
    elif oper == 2:
        print(n1 * n2)
    elif oper == 3:
        print(n1 / n2)
    else:
        print("Invalid Input")







    restart = input("\nWould you like to restart this program?  ")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("ok bye ....Goodbye.")


script()


