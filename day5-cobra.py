from os import system
system("cls")


try:
    n:int = int(input("Input from (1-20): "))

    if n <= 20 and n > 0:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(f"{(i * j):4}", end=" ")
            print()
    else:
        print("Invalid input please input from 1-20 only")
except:
    print("Inavlid input")