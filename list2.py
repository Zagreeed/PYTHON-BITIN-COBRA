"""
	list 
"""
from os import system

mlist:list = [1,2,3,4,5,6,7,8]

def main()->None: 
    system('cls')
    print(mlist)
    #remove an item using pop() module of list
    # print(mlist.pop()) #remove the item at index 3
    # print(mlist)
    #inserting new item within the structure
    #insert the value 99, at index 5
    mlist.insert(5,'x')
    print(mlist)
    
    
if __name__=="__main__":
	main()