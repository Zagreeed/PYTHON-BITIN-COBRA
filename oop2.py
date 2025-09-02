'''
	Student class
'''
from oop1 import Person

class Student(Person):
    
    def __init__(self,idno:str,lastname:str,firstname:str,course:str,level:str)->None:
        super().__init__(lastname,firstname)
        self.idno = idno
        self.course = course
        self.level = level
        
    def setidno(self,idno:str)->None:       self.idno = idno
    def setcourse(self,course:str)->None:   self.course = course
    def setlevel(self,level:str)->None:     self.level = level
    #
    def getidno(self)->str:                 return self.idno
    def getcourse(self)->str:               return self.course
    def getlevel(self)->str:                return self.level
    #
    def __str__(self)->str:
        return self.idno +" "+super().__str__()+" "+self.course+" "+self.level
    #
    def __eq__(self,other)->bool:
        ok:bool = False
        if isinstance(other,Student):
            if self.idno == other.idno:
                ok = True
        return ok

def main()->None:
    s = Student("0001","alpha","bravo","bscpe","2")
    t = Student("0001","charlie","delta","bsca","3")
    u = Student("0003","echo","foxtrot","bscream","1")
    v = Student("0004","golf","hotel","bshm","2")
    #
    print(s)
    print(t)
    print(u)
    print(v)
    print(s.__eq__(t))
    t.setidno("0009")
    print(s.__eq__(t))
    
if __name__=="__main__":
    main()
    
    
    
    
        
    
    
    
    
    
    
    