'''
      database helper
'''  

from os import system
from sqlite3 import connect,Row

database:str = 'users.db'


def getall(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    return getprocess(sql,[])

def getrecord(table:str, **kwargs)->list:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`=?"
    return getprocess(sql,vals)
   
def addrecord(table:str, **kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fields:str = "`,`".join(keys)
    data:str = "','".join(vals)
    sql:str = f"INSERT INTO `{table}`(`{fields}`) VALUES('{data}')"
    return postprocess(sql)
   
def deleterecord(table:str, **kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}`=?"
    return postprocess(sql,vals)
   
def updaterecord(table:str, **kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fields:list = []
    newvals:list = []
    for index in range(1, len(vals)):
        fields.append(f"`{keys[index]}`=?")
        newvals.append(vals[index])
    flds:str = ",".join(fields)
    sql:str = f"UPDATE `{table}` SET {flds} WHERE `{keys[0]}`=?"
    newvals.append(vals[0])
    return postprocess(sql,newvals)
   
def uservalidate(table:str, **kwargs)->list:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"SELECT * FROM `{table}` where `{keys[0]}`=? AND `{keys[1]}`=?"
    return getprocess(sql,vals)

def getprocess(sql:str,vals:list=[])->list:
    conn:any = connect(database)
    conn.row_factory = Row
    cursor:any = conn.cursor()
    cursor.execute(sql,vals)
    data:list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
   
def postprocess(sql:str,vals:list=[])->bool:
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql,vals)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False
   

def main()->None:
    system('cls')
    data:list = getall('users')
    for item in data:
        print(item['id'],end=" ")
        print(item['username'],end=" ")
        print(item['password'])
       
   
if __name__ == "__main__":
    main()

