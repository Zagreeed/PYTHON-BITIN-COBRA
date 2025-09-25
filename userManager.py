
'''
User management system
'''
from os import system
from pwinput import pwinput
from dbhelper import *


def displayusers()->None:
    system('cls')
    
    users:list = getall('users')
    if len(users) == 0:
        print(' '*74)
        print("User list is empty!".center(74, ' '))
        return
    
    print(' '*74)
    print("User List".center(74, ' '))
    print(' '*14 + '-'*50)
    print(f"{'ID':<8} {'USERNAME':<15} {'PASSWORD':<15}".center(74,' '))
    print(' '*11 + '-'*50)
    
    for user in users:
        print(f"{user['id']:<8} {user['username']:<15} {user['password']:<15}".center(74, ' '))


def finduser()->None:
    system('cls')
    if len(getall('users')) == 0:
        print(' '*74)
        print("There are no users in the database!".center(74,' '))
        return

    try:
        print(' '*74)
        print("Find User".center(74,' '))
        print(' ' * 24 + '-'*20)
        idNo = input(' ' * 28 + "Enter User ID: ")
        data = getrecord('users', id=idNo)

        if len(data) > 0:
            system('cls')
            print(' '*74)
            print("User Found:".center(74,' '))
            print(' '*12 + '-'*50)
            print(f"{'ID':<6} {'USERNAME':<15} {'PASSWORD':<15}".center(74,' '))
            print(('-'*50).center(74, ' '))
            for user in data:
                print(f"{user['id']:<6} {user['username']:<15} {user['password']:<15}".center(74,' '))
        else:
            print(' '*74)
            print(f"User with ID {idNo} not found!".center(74,' '))
    except Exception as e:
        print(' '*74)
        print("Error finding user! Please try again.".center(74,' '))


def adduser()->bool:
    system('cls')
    try:
        print(' '*74)
        print("Enter User Details".center(74,' '))
        print(' ' * 24 + '-'*26)

        username = input(' ' * 26 + "Username: ")
        
        # Check if username already exists
        existing_users = getall('users')
        for user in existing_users:
            if user['username'] == username:
                print(' '*74)
                print(f"User '{username}' already exists!".center(74, ' '))
                return False

        password = input(' ' * 27 + "Password: ")
        
        success = addrecord("users", username=username, password=password)
        
        if success:
            print(' '*74)
            print(f"User {username} added successfully!".center(74,' '))
            return True
        else:
            print(' '*74)
            print("Failed to add user!".center(74,' '))
            return False
        
    except Exception as e:
        print(' '*74)
        print("Error adding user! Please try again.".center(74,' '))
        return False


def deleteuser()->bool:
    system('cls')
    
    if len(getall('users')) == 0:
        print(' '*74)
        print("User list is empty!".center(74, ' '))
        return False
        
    try:
        print(' '*74)
        print("Delete User".center(74,' '))
        print(' ' * 24 + '-'*20)
        idNo = input(' ' * 28 + "Enter ID to delete: ")
        
        # Find user first
        data = getrecord('users', id=idNo)
        
        if len(data) == 0:
            print(' ' * 74)
            print(f"User with ID '{idNo}' not found!".center(74, ' '))
            return False
            
        user = data[0]
        print(' '*74)
        print("User to be deleted:".center(74,' '))
        print(' '*12 + '-'*50)
        print(f"{'ID':<6} {'USERNAME':<15} {'PASSWORD':<15}".center(74,' '))
        print(('-'*50).center(74, ' '))
        print(f"{user['id']:<6} {user['username']:<15} {user['password']:<15}".center(74,' '))
        print(' '*74)

        confirm = input(' ' * 25 + "Confirm deletion? (y/n): ").lower()
        if confirm == 'y' or confirm == 'yes':
            success = deleterecord('users', id=idNo)
            if success:
                print(' '*74)
                print("User deleted successfully!".center(74,' '))
                return True
            else:
                print(' '*74)
                print("Failed to delete user!".center(74,' '))
                return False
        else:
            print(' '*74)
            print("Deletion cancelled.".center(74,' '))
            return False
            
    except Exception as e:
        print(' '*74)
        print("Error deleting user! Please try again.".center(74,' '))
        return False


def updateuser()->bool:
    system('cls')
    
    if len(getall('users')) == 0:
        print(' '*74)
        print("User list is empty!".center(74, ' '))
        return False

    try:
        print(' '*74)
        print("Update User".center(74,' '))
        print(' ' * 24 + '-'*20)
        idNo = input(' ' * 28 + "Enter User ID to update: ")
         
        data = getrecord('users', id=idNo)
        
        if len(data) == 0:
            print(' '*74)
            print(f"User with ID {idNo} not found!".center(74,' '))
            return False
            
        user = data[0]
        print(' '*74)
        print("Current User Details:".center(74,' '))
        print(' '*12 + '-'*50)
        print(f"{'ID':<6} {'USERNAME':<15} {'PASSWORD':<15}".center(74,' '))
        print(' '*12 + '-'*50)
        print(f"{user['id']:<6} {user['username']:<15} {user['password']:<15}".center(74,' '))
    
        print(' '*74)
        print("Enter New Details (press Enter to keep current):".center(74,' '))
        print(' '*12 + '-'*50)
        
        new_username = input(' ' * 26 + f"Username ({user['username']}): ")
        new_password = input(' ' * 27 + f"Password ({user['password']}): ")
        
        # Keep current values if empty input
        if new_username.strip() == "":
            new_username = user['username']
        if new_password.strip() == "":
            new_password = user['password']

        # Check if new username already exists (but not the current user)
        existing_users = getall('users')
        for existing_user in existing_users:
            if existing_user['username'] == new_username and existing_user['id'] != user['id']:
                print(' '*74)
                print(f"Username '{new_username}' already exists!".center(74, ' '))
                return False

        success = updaterecord('users', id=idNo, username=new_username, password=new_password)
        
        if success:
            print(' '*74)
            print(f"User {new_username} updated successfully!".center(74,' '))
            return True
        else:
            print(' '*74)
            print("Failed to update user!".center(74,' '))
            return False
        
    except Exception as e:
        print(' '*74)
        print("Error updating user! Please try again.".center(74,' '))
        return False


def displaymenu()->None:
    system('cls')
    for i in range(1,4):print(' '*74)    
    print('- User Management System -'.center(74,' '))
    print(' '*24,end="")
    print('-'*26)
    print('1. Add User               '.center(74,' '))
    print('2. Find User              '.center(74,' '))
    print('3. Delete User            '.center(74,' '))
    print('4. Update User            '.center(74,' '))
    print('5. Display All Users      '.center(74,' '))
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
            print(' '*74)
            print("Invalid Input! Please enter a number.".center(74, ' '))


def main()->None:
    system('cls')
    print(' '*74)
    print(' User Login '.center(74,'-')) 
    username:str = input(' ' * 24 + "USERNAME: ")
    password:str = pwinput(' ' * 24 + "PASSWORD: ")
    
    # Validate login
    user:list = uservalidate('users', username=username, password=password)
    message:str = "LOGIN ACCEPTED" if len(user) > 0 else "LOGIN FAILED"
    print(' '*74)
    print(message.center(74, ' '))
    input(' ' * 20 + "Press any key to continue....")
    
    if message == "LOGIN ACCEPTED":
        while True:
            displaymenu()
            
            value = getInput()

            match value:
                case 0:
                    print(' '*74)
                    print("Thank you for using User Management System!".center(74,' '))
                    print("Goodbye!".center(74,' '))
                    break
                case 1:
                    adduser()
                    
                case 2:
                    finduser()
                    
                case 3:
                    deleteuser()
                    
                case 4:
                    updateuser()
                    
                case 5:
                    displayusers()
                    
                case _:
                    print(' '*74)
                    print("Invalid choice! Please select 0-5.".center(74,' '))
            
            if value != 0:
                print(' '*74)
                input("Press Enter to continue...".center(74,' '))
    else:
        print(' '*74)
        print("Access denied. Exiting...".center(74, ' '))
    
    
if __name__=="__main__":
    main()