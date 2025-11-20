
import sqlite3

def dbconnect()->any:

    conn = sqlite3.connect('students.db')
    # This makes rows behave like dictionaries
    conn.row_factory = sqlite3.Row
    return conn

def getprocess(sql:str,vals:list)->list:
    conn:any = dbconnect()
    cursor:any = conn.cursor()
    cursor.execute(sql,vals)
    # Convert Row objects to dictionaries
    data:list = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return data
    
def postprocess(sql:str,vals:list)->bool:
    ok:bool = False
    conn:any = dbconnect()
    cursor:any = conn.cursor()
    try:
        cursor.execute(sql,vals)
        conn.commit()
        ok=True if cursor.rowcount>0 else False
    except Exception as e:
        print(f"Error:{e}")
    finally:
        cursor.close()
        conn.close()
        return ok
    
def getall(table:str)->list:
    sql:str = f"SELECT * FROM {table}"
    return getprocess(sql,[])
    
def getrecord(table:str,**kwargs)->list:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:list = []
    for key in keys:
        flds.append(f"{key}=?")
    fields:str = " AND ".join(flds)
    sql:str = f"SELECT * FROM {table} WHERE {fields}"
    return getprocess(sql,vals)
    
def addrecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    qmark:list = ['?']*len(vals)
    dta:str=",".join(qmark)
    fields:str = ",".join(keys)
    sql:str = f"INSERT INTO {table}({fields}) VALUES({dta})"
    return postprocess(sql,vals)
    
def deleterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:list = []
    for key in keys:
        flds.append(f"{key}=?")
    fields:str = " AND ".join(flds)
    sql:str = f"DELETE FROM {table} WHERE {fields}"
    return postprocess(sql,vals)
    
def updaterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    newvals:list = []
    flds:list = []
    for index in range(1,len(keys)):
        flds.append(f"{keys[index]}=?")
        newvals.append(vals[index])
    fields:str = ",".join(flds)
    # Add the first value for WHERE clause
    newvals.append(vals[0])
    sql:str = f"UPDATE {table} SET {fields} WHERE {keys[0]}=?"
    return postprocess(sql,newvals)