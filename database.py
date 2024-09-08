import pymysql
from tkinter import messagebox


def db_connect():
  global cursor,connection
  try:
    connection=pymysql.connect(host="localhost",user="root",password="root@123")
    cursor=connection.cursor()
    print("db connected")
  except:
    messagebox.showerror("Error","Database not connected!")
    return
  cursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
  cursor.execute("USE employee_data")
  cursor.execute("CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50), Phone VARCHAR(15), Role VARCHAR(50), Gender VARCHAR(20),Salary int(10))")

def insert(id,name,phone,role,gender,salary):
  cursor.execute(r"INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
  connection.commit()
  
  

def id_exists(id):
  cursor.execute(r"SELECT count(*) FROM data WHERE id=%s",id)
  count=cursor.fetchone()
  if count[0]>0:
    return True
  return False

def fetch_all():
  cursor.execute("SELECT * FROM data")
  result=cursor.fetchall()
  return result

def update(id,name,phone,role,gender,salary):
  cursor.execute(r"UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s",(name,phone,role,gender,salary,id))
  connection.commit()

def delete(id):
  cursor.execute(r"DELETE FROM data WHERE id=%s",(id))
  connection.commit()

def delete_all():
  cursor.execute("DELETE FROM data")
  connection.commit()

def fetch_some(key,val):

  query="SELECT * FROM data WHERE "+key+r" = %s"
  cursor.execute(query,val)
  result=cursor.fetchall()

  return result
                            
db_connect()