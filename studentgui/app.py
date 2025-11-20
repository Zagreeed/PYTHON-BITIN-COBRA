'''
	Student GUI App
'''
from dbhelper import *

import tkinter as tk
from tkinter import ttk,messagebox

class StudentList:
    def __init__(self)->None:
        self.root = tk.Tk()

        self.root.resizable(False, False)

        self.root.iconbitmap("images/ccslogo1.ico")
        self.root.title("Danley Yap, Galan")
        self.root.configure(background='gray')

 

        self.root.resizable(False,False)
        self.centerwindow()
        self.showlist()
        self.showform()
        self.root.mainloop()
        
        
    def centerwindow(self)->None:
        width:int = 800
        height:int = 380
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x:int = (screen_width-width)//2
        y:int = (screen_height-height)//2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def showlist(self)->None:
        self.frame1 = tk.Frame(self.root)
        self.frame1.grid(row=0,column=1)
        self.tv = ttk.Treeview(self.frame1,column=('idno','lastname','firstname','course','level'),show='headings')
        self.tv.grid(row=0,column=1,padx=5,pady=20)
        #set column sizes and orientation of items
        self.tv.column('idno',anchor='c',width=100)
        self.tv.column('lastname',anchor='w',width=100)
        self.tv.column('firstname',anchor='w',width=100)
        self.tv.column('course',anchor='w',width=100)
        self.tv.column('level',anchor='c',width=100)
        #set the column labels
        self.tv.heading('idno',text='IDNO')
        self.tv.heading('lastname',text='LASTNAME')
        self.tv.heading('firstname',text='FIRSTNAME')
        self.tv.heading('course',text='COURSE')
        self.tv.heading('level',text='LEVEL')
        #
        self.tv.bind("<<TreeviewSelect>>",self.on_item_select)
        #populate the table
        students:list = getall('students')
        self.count=0
        for student in students:
            self.tv.insert('','end','iid'+str(self.count),values=(f"{student['idno']}",f"{student['lastname'].upper()}",f"{student['firstname'].upper()}",f"{student['course'].upper()}",f"{student['level']}"))
            self.count+=1
    
    def on_item_select(self,event)->None:
        selected_item = self.tv.selection()
        for itemid in selected_item:
            self.itemid=itemid
            items_values=list(self.tv.item(itemid,'values'))
            print(items_values)
            self.clearform()
            self.txt['idno'].insert(0,items_values[0])
            self.txt['lastname'].insert(0,items_values[1])
            self.txt['firstname'].insert(0,items_values[2])
            self.cbo['course'].insert(0,items_values[3])
            self.cbo['level'].insert(0,items_values[4])
            
            
    def showform(self)->None:
        self.frame2 = tk.LabelFrame(self.root,text="STUDENT INFORMATION")
        self.frame2.grid(row=0,column=0,padx=10,pady=50)
        #
        labels:list=['idno','lastname','firstname','course','level']
        
        lbl:dict={}
        self.txt:dict={}
        self.cbo:dict={}
        
        row:int = 0
        for label in labels:
            lbl[label]=tk.Label(self.frame2,text=label.upper()).grid(row=row,column=0,padx=10,pady=10,sticky="w")
            row+=1
        
        self.txt['idno'] = tk.Entry(self.frame2,width=23)    
        self.txt['idno'].grid(row=0,column=1,padx=10)
        self.txt['lastname'] = tk.Entry(self.frame2,width=23)
        self.txt['lastname'].grid(row=1,column=1,padx=10)
        self.txt['firstname'] = tk.Entry(self.frame2,width=23)
        self.txt['firstname'].grid(row=2,column=1,padx=10)
        self.cbo['course'] = ttk.Combobox(self.frame2,values=('BSIT','BSCS','BSCPE','BSHM','BSCJ','BSE'))
        self.cbo['course'].grid(row=3,column=1,padx=10)
        self.cbo['level'] = ttk.Combobox(self.frame2,values=('1','2','3','4'))
        self.cbo['level'].grid(row=4,column=1,padx=10)
        #
        self.buttonframe=tk.Frame(self.frame2)
        self.buttonframe.grid(row=5,column=0,columnspan=2,pady=10)
        #
        self.btnsave=tk.Button(self.buttonframe,text=" SAVE ",bg='blue',fg='white',command=self.save)
        self.btnsave.grid(row=0,column=0,padx=10)

        
        self.btndelete=tk.Button(self.buttonframe,text=" DELETE ",bg='red',fg='white',command=self.delete_item)
        self.btndelete.grid(row=0,column=1,padx=10)

        self.btnnew=tk.Button(self.buttonframe,text=" NEW ",bg='green',fg='white',command=self.clearform)
        self.btnnew.grid(row=0,column=3,padx=10)

    
    def delete_item(self)->None:
        idno:str = self.txt['idno'].get()
        if idno.isdigit():
            ok:bool = deleterecord('students',idno=idno)
            if ok:
                messagebox.showinfo('INFORMATION','STUDENT DELETED')
                self.tv.delete(self.itemid)
                self.clearform()
        else:
            messagebox.showwarning('WARNING','IDNO SHOULD BE NUMERIC')
    
    
    def save(self)->None:
        idno:str = self.txt['idno'].get()
        lastname:str = self.txt['lastname'].get()
        firstname:str = self.txt['firstname'].get()
        course:str = self.cbo['course'].get()
        level:str = self.cbo['level'].get()
        #validation
        if idno!="" and lastname!="" and firstname!="" and course!="" and level!="":
            if idno.isdigit():
                ok:bool = addrecord('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
                if ok:
                
                    self.tv.insert('','end','iid'+str(self.count),values=(idno,lastname.upper(),firstname.upper(),course.upper(),level))
                    self.count+=1  # Don't forget to increment the counter!
                    messagebox.showinfo('INFORMATION','NEW STUDENT ADDED')
                else:
                    messagebox.showwarning('WARNING','ERROR ADDING STUDENT (Duplicate IDNO?)')
            else:
                messagebox.showwarning('WARNING','IDNO SHOULD BE NUMERIC')
        else:
            messagebox.showwarning('WARNING','FILL ALL FIELDS')
        
        self.clearform()
        
        
    def clearform(self)->None:   
        self.txt['idno'].delete(0,tk.END)
        self.txt['lastname'].delete(0,tk.END)
        self.txt['firstname'].delete(0,tk.END)
        self.cbo['course'].delete(0,tk.END)
        self.cbo['level'].delete(0,tk.END)
        self.txt['idno'].focus_set()
        
def main()->None:
    StudentList()
    
if __name__=="__main__":
    main()