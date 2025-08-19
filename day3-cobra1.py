# A program that would accept a positive integer not greater
# than 20 and dislay it from 1 until the inpute string

from os import system

system("cls")



while(True):

    try:

      
        n:int = int(input("Input a integer from 1 to 20: "))

        if n > 0 and n < 20:
            for i in range(1,n + 1):
                print(i, end=" ")
       

            print("")

            for i in reversed(range(1, n + 1)):    
                print(i, end=" ")

            print("")
            print("EVEN")

            for i in range(1, n + 1):
                if i%2 == 0:
                    print(i, end=" ")

            print("")
            print("ODD")

            for i in range(1, n + 1):
                if i%2 != 0:
                    print(i, end=" ")

            break
        else:
            print("Number must be less than 20 and greater than 0")
        
    except:
        print("Invalid input")
