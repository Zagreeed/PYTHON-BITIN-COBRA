'''
	Person class
'''
class Person:
	#constructor
    def __init__(self,lastname:str,firstname:str)->None:
        self.lastname = lastname
        self.firstname= firstname
	#setters
    def setlastname(self,lastname:str)->None: 
        self.lastname = lastname
    def setfirstname(self,firstname)->None: 
        self.firstname= firstname
    #getters
    def getlastname(self)->str:
        return self.lastname
    def getfirstname(self)->str:
        return self.firstname
    #toString()
    def __str__(self)->str:
        return f"{self.lastname.upper():<10} {self.firstname:<10}"
        
        