'''
	Student List app
'''
from os import system
from studentlist import StudentList
from student import Student

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(' '*74)    
    print('- StudentList Management -'.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    print('1. Create StudentList     '.center(74,' '))
    print('2. Add Student            '.center(74,' '))
    print('3. Find Student           '.center(74,' '))
    print('4. Delete Student         '.center(74,' '))
    print('5. Update Student         '.center(74,' '))
    print('0. Quit/End               '.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    for i in range(1,3):print(' '*74) 

def main()->None: 
    displaymenu()

if __name__=="__main__":
	main()
