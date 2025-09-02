class Person:
    
    def __init__(self,lastname:str,firstname:str)->None:
        self.lastname = lastname
        self.firstname = firstname
        
    #setter - modifier function/module
    def setLastname(self,lastname:str)->None:
        self.lastname = lastname
    def setFirstname(self,firstname:str)->None:
        self.firstname = firstname
    
    #getter - accessors
    def getLastname(self)->str:
        return self.lastname
    
    def getFirstname(self)->str:
        return self.firstname
    
    def __str__(self)->str:
        return self.lastname+" "+self.firstname
        
    def __eq__(self,other)->bool:
        ok:bool = False
        if isinstance(other,Person):
            if self.lastname == other.lastname and self.firstname == other.firstname:
                ok = True
        return ok
        
	
def main()->None:
    p = Person("durano","dennis")
    q = Person("durano","alpha")
    print(p)
    # p.setLastname("hello")
    # p.setFirstname("world")
    print(q)
    
    ok:bool = p.__eq__(q)
    print(ok)
    
    
    
if __name__=="__main__":  
    main()