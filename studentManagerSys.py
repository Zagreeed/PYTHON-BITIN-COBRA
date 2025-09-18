from os import system
from student import Student
filename:str ="student.csv"
slist:list = []     #local data container
#procedural method
def loader()->None: pass
    
def updater()->None:pass
def addstudent(student:Student)->bool:pass
    
def findstudent(idno:str)->Student:pass
    
def deletestudent(idno:str)->bool:pass
    
def updatestudent(student:Student)->bool:pass
    
#
def displaylist()->None:pass
#
def displaymenu()->None:
    system('cls')
    for i in range(1,4):print(' '*74)    
    print('- StudentList Management -'.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    print('1. Create StudentList     '.center(74,' '))
    print('2. Add Student            '.center(74,' '))
    print('3. Find Student           '.center(74,' '))
    print('4. Delete Student         '.center(74,' '))
    print('5. Update Student         '.center(74,' '))
    print('6. Display All Student    '.center(74,' '))
    print('0. Quit/End               '.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    for i in range(1,3):print(' '*74) 
    
def main()->None:
    displaymenu()
    
#launcher condition
if __name__=="__main__":
    main()