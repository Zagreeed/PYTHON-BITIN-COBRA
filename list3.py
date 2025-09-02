'''
	slicing the list
    mlist[start:end:step]
'''
from os import system

mlist:list = [1,2,3,4,5,6,7,8]

def main()->None:
    system('cls')
    print(mlist)
    for i in range(0,4):
        print(mlist[i],end=" ")
    print()
    print(mlist[0:4])
    print(mlist[-8])
    #display 8 7 6 5 4
    newlist=mlist[-1:-6:-1]
    for item in newlist: print(item)
    #display the list in reverse order
    print(mlist[-4::])
    #display all even values in the list using
    print(mlist[1::2])
    
    
    
    
if __name__=="__main__":
    main()
    
    