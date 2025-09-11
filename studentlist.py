'''
	StudentList
'''
from student import Student
from os import system

class StudentList:
    def __init__(self,size)->None:
        self.slist = [] #data container
        self.size = size #limiting element
        
    #sentinel modules
    def isfull(self)->bool:
        return len(self.slist) == self.size
        
    def isempty(self)->bool: 
        return len(self.slist) == 0
        
    #utility methods
    def addstudent(self,s:Student)->bool:
        ok:bool = not self.isfull()
        if ok:
            self.slist.append(s)
        return ok
    
    def findstudent(self,idno:str)->Student:
        ok:bool = not self.isempty()
        s:Student = None
        if ok:
            for student in self.slist:
                if student.getidno() == idno:
                    s=student
                    break #stop the loop
        return s
    
    def deletestudent(self,idno:str)->bool:
        s:Student = self.findstudent(idno)
        ok:bool = False
        if s != None:
            ok = True
            self.slist.remove(s)
        return ok
    
    def updatestudent(self,s:Student)->bool:
        student:Student = self.findstudent(s.getidno())
        ok:bool = False
        if student != None:
            index:int = self.slist.index(student)
            self.slist[index] = s
            ok = True
        return ok
    
    def showlist(self)->None:
        if not self.isempty():
            for student in self.slist:
                print(student)
        else:
            print("list is empty !!!")
        
        
def main()->None:
    system('cls')
    mylist = StudentList(10)
    print(mylist.addstudent(Student('0001','alpha','bravo','bsit','3')))
    print(mylist.addstudent(Student('0002','charlie','delta','bscs','2')))
    print(mylist.addstudent(Student('0003','echo','foxtrot','bscream','4')))
    print(mylist.addstudent(Student('0004','golf','hotel','bshm','1')))
    mylist.showlist()
    print()
    print(mylist.findstudent('0001'))
    print()
    print(mylist.deletestudent('0002'))
    print()
    mylist.showlist()
    print()
    print(mylist.updatestudent(Student('0004','xxx','xxx','xx','1')))
    print()
    mylist.showlist()
    
if __name__=="__main__":
    main()
        
        
            
        
        
        
        
    