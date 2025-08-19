"""
    a program that accept a string
    
    
    name: popop
    hello: popop

"""


from os import system
system("cls")

name:str = input("Enter your pagalan: ")
birth:int = int(input("Put your year of birth: "))


age = 2025 - birth


for i in range(5):
    print("your name is " + name + " and your current age is ", age ) 
