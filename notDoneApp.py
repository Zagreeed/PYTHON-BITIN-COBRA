'''
	Student List app
'''
from os import system
from studentlist import StudentList
from student import Student

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

def getInput():
    while True:
        try:
            val = int(input(' ' * 24 + "###: "))
            return val
        except ValueError: 
            print("Invalid Input! Please enter a number.".center(74, ' '))

def creatList(size:int)->StudentList:
     studList = StudentList(size)
     return studList

def addstudent(list:StudentList)->None:
    if list == None:
        print("Please create a StudentList first!".center(74,' '))
        return
    
    if list.isfull():
        print("StudentList is full! Cannot add more students.".center(74,' '))
        return
    
    try:
        print(' '*74)
        print("Enter Student Details".center(74,' '))
        print(' ' * 24 + '-'*20)
        idNo = input(' ' * 27 + "Id Number: ")
        firstName = input(' ' * 26 + "First Name: ")
        lastName = input(' ' * 27 + "Last Name: ")
        course = input(' ' * 30 + "Course: ")
        year = input(' ' * 32 + "Year: ")
        
      
        if list.findstudent(idNo) != None:
            print(f"Student with ID {idNo} already exists!".center(74,' '))
            return
            
        if list.addstudent(Student(idNo, lastName, firstName, course, year)):
            print(' '*74)
            print(f"Student {idNo} {firstName} {lastName} successfully added!".center(74,' '))
        else:
            print("Failed to add student!".center(74,' '))
            
    except Exception as e:
        print("Error adding student! Please try again.".center(74,' '))

def findstudent(list:StudentList)->None:
    if list == None:
        print("Please create a StudentList first!".center(74,' '))
        return
    
    if list.isempty():
        print("StudentList is empty!".center(74,' '))
        return
        
    try:
        print(' '*74)
        idNo = input(' ' * 24 + "Enter ID to find: ")
        student = list.findstudent(idNo)
        
        if student != None:
            print(' '*74)
            print("Student Found:".center(74,' '))
            print(' '*14 + '-'*50)
            print(f"{'ID':<10} {'LASTNAME':<12} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
            print(('-'*50).center(74, ' '))
            print(str(student).center(74,' '))
        else:
            print(f"Student with ID {idNo} not found!".center(74,' '))
            
    except Exception as e:
        print("Error finding student! Please try again.".center(74,' '))

def deletestudent(list:StudentList)->None:
    if list == None:
        print("Please create a StudentList first!".center(74,' '))
        return
    
    if list.isempty():
        print("StudentList is empty! Nothing to delete.".center(74,' '))
        return
        
    try:
        print(' '*74)
        idNo = input(' ' * 28 + "Enter ID to delete: ")
        
        
        student = list.findstudent(idNo)
        if student == None:
            print(f"Student with ID {idNo} not found!".center(74,' '))
            return
            
        
        print(' '*74)
        print("Student to be deleted:".center(74,' '))
        print(' '*14 + '-'*22)
        print(str(student).center(74,' '))
        print(' '*74)
        
        confirm = input(' ' * 25 + "Confirm deletion (y/n): ").lower()
        if confirm == 'y' or confirm == 'yes':
            if list.deletestudent(idNo):
                print(' '*74)
                print(f"Student {idNo} deleted successfully!".center(74,' '))
            else:
                print("Failed to delete student!".center(74,' '))
        else:
            print("Deletion cancelled.".center(74,' '))
            
    except Exception as e:
        print("Error deleting student! Please try again.".center(74,' '))

def updatestudent(list:StudentList)->None:
    if list == None:
        print("Please create a StudentList first!".center(74,' '))
        return
    
    if list.isempty():
        print("StudentList is empty! Nothing to update.".center(74,' '))
        return
        
    try:
        print(' '*74)
        idNo = input(' ' * 28 + "Enter ID to update: ")
        
        # Check if student exists
        student = list.findstudent(idNo)
        if student == None:
            print(f"Student with ID {idNo} not found!".center(74,' '))
            return
            
        # Show current student details
        print(' '*74)
        print("Current Student Details:".center(74,' '))
        print(' '*14 + '-'*22)
        print(str(student).center(74,' '))
        print(' '*74)
        
        print("Enter New Details (press Enter to keep current):".center(74,' '))
        print('-'*48)
        
     
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
        
        updated_student = Student(idNo, new_lastName, new_firstName, new_course, new_year)
        
        if list.updatestudent(updated_student):
            print(' '*74)
            print(f"Student {idNo} updated successfully!".center(74,' '))
        else:
            print("Failed to update student!".center(74,' '))
            
    except Exception as e:
        print("Error updating student! Please try again.".center(74,' '))

def displaystudent(list:StudentList)->None:
    if list == None:
        print("Please create a StudentList first!".center(74,' '))
        return
    
    if list.isempty():
        print("StudentList is empty!".center(74,' '))
        return
        
    try:
        print(' '*74)
        print("All Students:".center(74,' '))
        print(' '*14 + '-'*13)
        print(' '*74)
        print(f"{'ID':<10} {'LASTNAME':<12} {'FIRSTNAME':<12} {'COURSE':<10} {'YEAR':>5}".center(74,' '))
        print('-'*50)
        
        for student in list.slist:
            print(str(student).center(74,' '))
            
        print(' '*74)
        print(f"Total Students: {len(list.slist)}/{list.size}".center(74,' '))
        
    except Exception as e:
        print("Error displaying students! Please try again.".center(74,' '))

def main()->None: 
    list = None
    
    while True:
        displaymenu()
        if list != None:
            print(f"Current List: {len(list.slist)}/{list.size} students".center(74,' '))
        print(' '*74)
        
        value = getInput()

        match value:
            case 0:
                print(' '*74)
                print("Thank you for using StudentList Management!".center(74,' '))
                print("Goodbye!".center(74,' '))
                break
                
            case 1:
                try:
                    print(' '*74)
                    size = int(input(' ' * 24 + "Number of Students: "))
                    if size <= 0:
                        print("Size must be greater than 0!".center(74,' '))
                    else:
                        list = creatList(size)
                        print(' '*74)
                        print(' ' * 6 + f"StudentList of {size} created successfully!".center(74,' '))
                except ValueError:
                    print("Invalid input! Please enter a valid number.".center(74,' '))
                    
            case 2:
                addstudent(list)
                
            case 3:
                findstudent(list)
                
            case 4:
                deletestudent(list)
                
            case 5:
                updatestudent(list)
                
            case 6:
                displaystudent(list)
                
            case _:
                print("Invalid choice! Please select 0-6.".center(74,' '))
        
        if value != 0:
            print(' '*74)
            input("Press Enter to continue...".center(74,' '))

if __name__=="__main__":
    main()
