from os import system
from student import Student


filename:str ="student.csv"
slist:list = []     #local data container
#procedural method


def loader()->None:
    slist.clear()

    file = open(filename)
    temp:list = file.readlines()
    for item in temp:
        fields = item.strip().split(',')
        slist.append(Student(fields[0], fields[1], fields[2], fields[3], fields[4]))
    file.close()
    
def updater()->None:

    if len(slist) >= 0:
        file = open(filename, 'w')
        
        for stud in slist:
            file.write(f"{stud.getidno()},{stud.getlastname()},{stud.getfirstname()},{stud.getcourse()},{stud.getlevel()}"+"\n")

        file.close()


def addstudent()->bool:
    system('cls')
    try:
        print(' '*74)
        print("Enter Student Details".center(74,' '))
        print(' ' * 24 + '-'*20)


        idNo = input(' ' * 27 + "Id Number: ")

        for stud in slist:
            if stud.getidno() == idNo:
                print(' '*74)
                print(f"Student with ID {idNo} already exists!".center(74, ' '))
                return False

        firstName = input(' ' * 26 + "First Name: ")
        lastName = input(' ' * 27 + "Last Name: ")
        course = input(' ' * 30 + "Course: ")
        year = input(' ' * 32 + "Year: ")
        

        slist.append(Student(idNo, lastName, firstName, course, year))
        updater()

        print(' '*74)
        print(f"Student {firstName} {lastName} added successfully".center(74,' '))
        
        return True
        
    except Exception as e:
        print("Error adding student! Please try again.".center(74,' '))
        return False
    
def findstudent()->Student:
    system('cls')
    if len(slist) == 0:
        print("There is no student!".center(74,' '))
        return

    try:
        print(' '*74)
        idNo = input(' ' * 24 + "Enter Student ID: ")
        student = None

        for stud in slist:
            if(stud.getidno() == idNo):
                student = stud
                break
            else:
                continue
        
        if student != None:
            system('cls')
            print(' '*74)
            print("Student Found:".center(74,' '))
            print(' '*12 + '-'*50)
            print(f"{'ID':<6} {'LASTNAME':<12} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
            print(('-'*50).center(74, ' '))
            print(str(student).center(74,' '))
        else:
            print(' '*74)
            print(f"Student with ID {idNo} not found!".center(74,' '))
    except Exception as e:
        print("Error finding student! Please try again.".center(74,' '))


def deletestudent()->bool:
    system('cls')

    if len(slist) == 0: 
        print("Student list is empty!".center(74, ' '))
        return False 
        
    try:
        print(' '*74)
        idNo = input(' ' * 28 + "Enter ID to delete: ")
        
        
        student = None
        index = None
        for i, stud in enumerate(slist):

            if stud.getidno() == idNo:
                student = stud
                index = i
                break
        

        if student is None:
            print(' ' * 74)
            print(f"Student with ID '{idNo}' not found!".center(74, ' '))
            return False
            
        
        print(' '*74)
        print("Student to be deleted:".center(74,' '))

        print(' '*12 + '-'*50)
        print(f"{'ID':<6} {'LASTNAME':<12} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
        print(('-'*50).center(74, ' '))

      
        print(str(student).center(74,' '))
        print(' '*74)

        
        confirm = input(' ' * 25 + "Confirm deletion? (y/n): ").lower()
        if confirm == 'y' or confirm == 'yes':
            
            del slist[index]
            print("Student deleted successfully!".center(74,' '))
            updater()
            return True
        else:
            print("Deletion cancelled.".center(74,' '))
            
    except Exception as e:
        print("Error deleting student! Please try again.".center(74,' '))

    
def updatestudent()->bool:
    
    system('cls')

    if len(slist) == 0: 
        print("Student list is empty!".center(74, ' '))
        return False

    try:
        print(' '*74)
        idNo = input(' ' * 28 + "Enter Student ID to update: ")
         
        student = None


        for stud in slist:
            if(stud.getidno() == idNo):
                student = stud
                break
            else:
                continue

        if student == None:
            print(f"Student with ID {idNo} not found!".center(74,' '))
            return
            

        print(' '*74)
        print("Current Student Details:".center(74,' '))
        print(' '*74)
        print("Student Found:".center(74,' '))
        print(' '*12 + '-'*50)
        print(f"{'ID':<6} {'LASTNAME':<12} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
        print(' '*12 + '-'*50)
        print(str(student).center(74,' '))
    
        print(' '*74)
        
        print("Enter New Details (press Enter to keep current):".center(74,' '))
        print(' '*12 + '-'*50)
        
     
        new_firstName = input(' ' * 26 + f"First Name ({student.getfirstname()}): ")
        new_lastName = input(' ' * 27 + f"Last Name ({student.getlastname()}): ")
        new_course = input(' ' * 30 + f"Course ({student.getcourse()}): ")
        new_year = input(' ' * 32 + f"Year ({student.getlevel()}): ")
        
      
        if new_firstName.strip() == "":
            new_firstName = student.getfirstname()
        if new_lastName.strip() == "":
            new_lastName = student.getlastname()
        if new_course.strip() == "":
            new_course = student.getcourse()
        if new_year.strip() == "":
            new_year = student.getlevel()


        for stud in slist:
            if(stud.getidno() == idNo):
                stud.setlastname(new_lastName)
                stud.setfirstname(new_firstName)
                stud.setcourse(new_course)
                stud.setlevel(new_year)

                # print(f"Student {stud.getfirstname()} {stud.getlastname()} successfully updated")
                print(' '*74)
                print(f"Student {stud.getfirstname()} updated successfully!".center(74,' '))
                break
            else:
                continue
        updater()        
        return True
        
            
    except Exception as e:
        print("Error updating student! Please try again.".center(74,' '))

    
def displaylist()->None:
    system('cls')

    if len(slist) == 0:
        print(' '*74)
        print("Student list is empty!".center(74, ' '))
        return
    
    print(' '*74)
    print("Student List".center(74, ' '))
    print(' '*14 + '-'*50)
    print(f"{'ID':<8} {'LASTNAME':<10} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
    print(' '*11 + '-'*60)
    
    for stud in slist:
        print(str(stud).center(74, ' '))


def displaymenu()->None:
    system('cls')
    for i in range(1,4):print(' '*74)    
    print('- Student Management System -'.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    print('1. Add Student            '.center(74,' '))
    print('2. Find Student           '.center(74,' '))
    print('3. Delete Student         '.center(74,' '))
    print('4. Update Student         '.center(74,' '))
    print('5. Display All Student    '.center(74,' '))
    print('0. Quit/End               '.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    for i in range(1,3):print(' '*74) 



def getInput():
    while True:
        try:
            val = int(input(' ' * 24 + "###: "))
            return val
        except ValueError: 
            print("Invalid Input! Please enter a number.".center(74, ' '))
    
def main()->None:
    loader()
    updater()
    while True:
        displaymenu()
        
        
        value = getInput()

        match value:
            case 0:
                print(' '*74)
                print("Thank you for using Student Management System!".center(74,' '))
                print("Goodbye!".center(74,' '))
                break
            case 1:
                addstudent()
                
            case 2:
                findstudent()
                
            case 3:
                deletestudent()
                
            case 4:
                updatestudent()
                
            case 5:
                displaylist()
                
            case _:
                print("Invalid choice! Please select 0-6.".center(74,' '))
        
        if value != 0:
            print(' '*74)
            input("Press Enter to continue...".center(74,' '))
    

if __name__=="__main__":
    main()