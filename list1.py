"""
	list 
"""
from os import system

mlist:list = [5,1,3,2,4]

def main()->None: 
    system('cls')
    print(mlist)
    # forward
    for i in range(0,len(mlist)):
        print(mlist[i],end=" ")
    print()
    # backward
    for i in range(len(mlist)-1,-1,-1):
        print(mlist[i],end=" ")
    print()
    mlist.sort(reverse=True) #arrange in descending order the elements
    for i in range(0,len(mlist)):
        print(mlist[i],end=" ")
        
    print()
    print(mlist[1])
    #using for each item loop
    for item in mlist:
        print(item,end=" ")
    print()
    
    
    

if __name__=="__main__":
	main()