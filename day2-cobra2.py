from os import system

system("cls")


def showMenu():
    print("-------MENU-------")
    print("1.Multiply")
    print("2.Divide")
    print("3.Add")
    print("4.Subtract")
    print("0.Quit/End")
    print("---------------------")


def calc(op):

    val1 = int(input("Enter Num1: "))
    val2 = int(input("Enter Num2: "))

    match op:
        case 1:
            print(f"{val1} * {val2} is equal to {val1 * val2}") 
        case 2:
           print(f"{val1} / {val2} is equal to {val1 / val2}") 
        case 3:
            print(f"{val1} + {val2} is equal to {val1 + val2}") 
        case 4:
            print(f"{val1} - {val2} is equal to {val1 - val2}") 



while(True):

    try:
        showMenu()

        val = int(input("Your Input: "))


        if(val > 4):
            print("Your inputed Num is greater than the options")

        if(val == 0):
            print("#####################")
            print("You exited the program")
            print("#####################")
            break

        if(val == 1):
            print("#####################")
            calc(1)
            print("#####################")
        if(val == 2):
            print("#####################")
            calc(2)
            print("#####################")
        if(val == 3):
            print("#####################")
            cal(3)
            print("#####################")
        if(val == 4):
            print("#####################")
            calc(4)
            print("#####################")
    except:
        print("Invalid Input")


   



