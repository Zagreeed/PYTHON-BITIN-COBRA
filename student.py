'''
	Student class
'''
from person import Person

class Student(Person):
    def __init__(self,idno:str,lastname:str,firstname:str,course:str,level:str)->None:
        super().__init__(lastname,firstname)
        self.idno = idno
        self.course = course
        self.level=level
    #setters
    def setidno(self,idno:str)->None:
        self.idno = idno
    def setcourse(self,course:str)->None:
        self.course = course
    def setlevel(self,level:str)->None:
        self.level=level
    #getters
    def getidno(self)->str:
        return self.idno
    def getcourse(self)->str:
        return self.course
    def getlevel(self)->str:
        return self.level
    #tostring
    def __str__(self)->str:
        return f"{self.idno:<10} {super().__str__()} {self.course:<10} {self.level:>5}"

def main()->None:
    s = Student('0001','durano','dennis','bscpe','4')
    print(s)
    t = Student('0002','hello','world','bsit','3')
    print(t)
    
    
if __name__=="__main__":
    main()
    