from os import system


def displayMenu()->None:
    system("cls")
    print("Main Menu".center(19, '-'))
    print("1. Multiply")
    print("2. Divide")
    print("3. Add")
    print("4. Subtract")
    print("0. Quit/End")
    print("-"*19)

def inputValue()->None:
    try:
        a:float = float(input("Enter first value: "))
        b:float = float(input("Enter first value: "))

        return a,b
    except Exception as e:
        print("Invalid Input: " + e)


def multiply(a:float, b:float)-> float: return a * b
def subtract(a:float, b:float)-> float: return a - b
def add(a:float, b:float)-> float: return a + b
def divide(a:float, b:float)-> float: return a / b
def quit()-> None:pass


def main()->None:
   
    option:str = "-1"

    while option != "0":
        displayMenu()
        option = input("Enter Option(0..4): ")

        match option:
            case "1": 
                system("cls")
                print("Multiply")
                print("-"*19)
                a,b = inputValue()
                print(f"The prodcut of {a} and {b} is {multiply(a,b)}")
            case "2": 
                system("cls")
                print("Divide")
                print("-"*19)
                a,b = inputValue()
                print(f"The quotient of {a} and {b} is {divide(a,b)}")
            case "3": 
                system("cls")
                print("Addition")
                print("-"*19)
                a,b = inputValue()
                print(f"The sum of {a} and {b} is {add(a,b)}")
            case "4": 
                system("cls")
                print("Subtraction")
                print("-"*19)
                a,b = inputValue()
                print(f"The prodcut of {a} and {b} is {subtract(a,b)}")
            case "0": quit()
            case _:  print("Inavlid Option")
            #
        input("\n Press any key to continue...")


if __name__ == "__main__":
    main()