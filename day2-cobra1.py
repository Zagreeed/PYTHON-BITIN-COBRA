from os import system

system("cls")




while(True):
    try:
        val = int(input("Inputn a value: "))


        if val == 0:
            print(val)
        else:

            # WAY 1
            # if val % 2 != 0:
            #     print(f"The number {val} is odd number")
            #     break
            # else:
            #     print(f"The number {val} is even numer")
            #     break

            # WAY 2
            print(f"---{val} num is an Odd number---" if  val % 2 != 0 else f"---{val} num is an number Even---")
            break
    except:
        print("Invalid input type")







