from os import system
system("cls")


def show():
    num1 = int(input("Input num1: "))
    num2 = int(input("Input num2: "))
   
    print(f"the sum of num1 and num2 is : {(num1 + num2)}")
    print(f"the difference of num1 and num2 is : {( num1 - num2)}")
    print(f"the produc of num1 and num2 is : {(num1 * num2)}")
    print(f"the quotient of num1 and num2 is : {(num1 / num2):.2f}")


try:
    show()
    
except:
    print("Dili puyde string dol")
    show()




