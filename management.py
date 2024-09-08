from customtkinter import *
from tkinter import messagebox,ttk
from PIL import Image
import database as db


def add_employee():

  if id_entry.get()=="" or name_entry.get()=="" or phone_entry.get()=="" or role_box.get()=="--select--" or gender_box.get()=="--select--" or salary_entry.get()=="":
    messagebox.showerror("Error","All fields are required!")

  elif db.id_exists(id_entry.get()):
    messagebox.showerror("Error","Id already exists!")

  else:
    db.insert(id_entry.get(),name_entry.get(),phone_entry.get(),role_box.get(),gender_box.get(),salary_entry.get())
    all_employees()
    messagebox.showinfo("Success","Employeee added successfully!")
    clear_data()

def clear_data():
  id_entry.delete(0, "end")
  name_entry.delete(0, "end")
  phone_entry.delete(0, "end")
  role_box.set("--select--")
  gender_box.set("--select--")
  salary_entry.delete(0, "end")


def all_employees():
  employees=db.fetch_all()
  tree.delete(*tree.get_children())
  for employee in employees:
    tree.insert("","end",values=employee)

def select_employee(event):
  index = tree.selection()
  if index:
    row=tree.item(index)["values"]

    clear_data()
    id_entry.insert(0,row[0])
    name_entry.insert(0,row[1])
    phone_entry.insert(0,row[2])
    role_box.set(row[3])
    gender_box.set(row[4])
    salary_entry.insert(0,row[5])

def update_employee():
  if id_entry.get()=="" or name_entry.get()=="" or phone_entry.get()=="" or role_box.get()=="--select--" or gender_box.get()=="--select--" or salary_entry.get()=="":
    messagebox.showerror("Error","All fields are required!")
  
  elif not db.id_exists(id_entry.get()):
    messagebox.showerror("Error","Employee does not exists!\nAdd them instead!")

  else:
    db.update(id_entry.get(),name_entry.get(),phone_entry.get(),role_box.get(),gender_box.get(),salary_entry.get())
    all_employees()
    messagebox.showinfo("Success","Employeee updated successfully!")
    clear_data()

def delete_employee():
  if id_entry.get()=="":
    messagebox.showerror("Error","Select an employee to delete!")
  elif not db.id_exists(id_entry.get()):
    messagebox.showerror("Error","Employee does not exists!")
  else:
    res=messagebox.askokcancel("Delete?","Employee data will be permanently deleted!")
    if res:
      db.delete(id_entry.get())
      all_employees()
      messagebox.showinfo("Success","Employee deleted successfully!")
      clear_data()

def delete_all():
  res=messagebox.askokcancel("Delete?","All employee data will be permanently deleted!")
  if res:
    db.delete_all()
  all_employees()

def search_input(event):
  
  global search_entry
  search_entry.destroy()

  if search_box.get() not in ("Role","Gender") :
    search_entry=CTkEntry(right_frame)
    search_entry.grid(row=0,column=1)
    return
  
  if search_box.get()=="Role":
    
    search_options=["Web Developer","Cloud Architect","Technical Writer","DevOps Engineer","Network Engineer","Data Scientist","Business Analyst","IT Consultant","UI/UX Desgner"]
      
  elif search_box.get()=="Gender":
    search_options=["Male","Female"]

  search_entry=CTkComboBox(right_frame,font=("Arial",15,"bold"),values=search_options,width=180,state="readonly")
  search_entry.set(search_options[0])
  search_entry.grid(row=0,column=1)


def search_employees():
  key,val=search_box.get(),search_entry.get()
  if key!="Search By" and val!="":
   
    employees=db.fetch_some(key,val)
    tree.delete(*tree.get_children())
    for employee in employees:
      tree.insert("","end",values=employee)
  else:
      messagebox.showerror("Error","Enter all fields for searching!") 


window = CTk()

window.geometry("1000x600")
window.resizable(0,0)
window.title("EMployee Management System")
window.configure(fg_color="#161c30")

image=CTkImage(Image.open("./imgs/main.png"),size=(1000,180))
image_label=CTkLabel(window,image=image,text="")
image_label.grid(row=0,column=0,columnspan=2)

left_frame=CTkFrame(window,fg_color="#161c30")
left_frame.grid(row=1,column=0)

id_label=CTkLabel(left_frame,text="Id",font=("Arial",18,"bold"),text_color="white")
id_label.grid(row=0,column=0,padx=20,pady=15,sticky="w")
id_entry=CTkEntry(left_frame,font=("Arial",18,"bold"),width=180)
id_entry.grid(row=0,column=1)

name_label=CTkLabel(left_frame,text="Name",font=("Arial",18,"bold"),text_color="white")
name_label.grid(row=1,column=0,padx=20,pady=15,sticky="w")
name_entry=CTkEntry(left_frame,font=("Arial",18,"bold"),width=180)
name_entry.grid(row=1,column=1)

phone_label=CTkLabel(left_frame,text="Phone",font=("Arial",18,"bold"),text_color="white")
phone_label.grid(row=2,column=0,padx=20,pady=15,sticky="w")
phone_entry=CTkEntry(left_frame,font=("Arial",18,"bold"),width=180)
phone_entry.grid(row=2,column=1)


role_label=CTkLabel(left_frame,text="Role",font=("Arial",18,"bold"),text_color="white")
role_label.grid(row=3,column=0,padx=20,pady=15,sticky="w")

role_options=["Web Developer","Cloud Architect","Technical Writer","DevOps Engineer","Network Engineer","Data Scientist","Business Analyst","IT Consultant","UI/UX Desgner"]
role_box=CTkComboBox(left_frame,font=("Arial",15,"bold"),values=role_options,width=180,state="readonly")
role_box.set("--select--")
role_box.grid(row=3,column=1)

gender_label=CTkLabel(left_frame,text="Gender",font=("Arial",18,"bold"),text_color="white")
gender_label.grid(row=4,column=0,padx=20,pady=15,sticky="w")

gender_options=["Male","Female"]
gender_box=CTkComboBox(left_frame,font=("Arial",15,"bold"),values=gender_options,width=180,state="readonly")
gender_box.set("--select--")
gender_box.grid(row=4,column=1)

salary_label=CTkLabel(left_frame,text="Salary",font=("Arial",18,"bold"),text_color="white")
salary_label.grid(row=5,column=0,padx=20,pady=15,sticky="w")
salary_entry=CTkEntry(left_frame,font=("Arial",18,"bold"),width=180)
salary_entry.grid(row=5,column=1)





right_frame=CTkFrame(window,fg_color="#161c30")
right_frame.grid(row=1,column=1)


search_options=["Id","Name","Role","Gender","Salary"]
search_box=CTkComboBox(right_frame,values=search_options,state="readonly",command=search_input)
search_box.set("Search By")
search_box.grid(row=0,column=0)

search_entry=CTkEntry(right_frame)
search_entry.grid(row=0,column=1)

search_button=CTkButton(right_frame,text="Search",width=100,font=("arial",18,"bold"),cursor="hand2",text_color="white",command=search_employees)
search_button.grid(row=0,column=2)

show_all_button=CTkButton(right_frame,text="Show All",width=100,font=("arial",18,"bold"),cursor="hand2",text_color="white",command=all_employees)
show_all_button.grid(row=0,column=3,pady=10)

tree=ttk.Treeview(right_frame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree["columns"]=["Id","Name","Phone","Role","Gender","Salary"]
tree.heading("Id",text="Id")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")

tree.config(show="headings")

tree.column("Id",width=100,anchor=CENTER)
tree.column("Name",width=160,anchor=CENTER)
tree.column("Phone",width=160,anchor=CENTER)
tree.column("Role",width=200,anchor=CENTER)
tree.column("Gender",width=100,anchor=CENTER)
tree.column("Salary",width=120,anchor=CENTER)

style=ttk.Style()
style.configure("Treeview.Heading",font=("arial",18,"bold"))
style.configure("Treeview",font=("arial",14,"bold"),rowheight=30,background="#161c30",foreground="white",fieldbackground="#161c30")

scroll_bar=ttk.Scrollbar(right_frame)
scroll_bar.grid(row=1,column=4,sticky="ns")

button_frame=CTkFrame(window,fg_color="#161c30")
button_frame.grid(row=2,column=0,columnspan=2)

new_button=CTkButton(button_frame,text="New Employee",font=("arial",18,"bold"),width=160,cursor="hand2",command=clear_data)
new_button.grid(row=0,column=0,pady=5,padx=10)

add_button=CTkButton(button_frame,text="Add Employee",font=("arial",18,"bold"),width=160,cursor="hand2",command=add_employee)
add_button.grid(row=0,column=1,pady=5,padx=10)

update_button=CTkButton(button_frame,text="Update Employee",font=("arial",18,"bold"),width=160,cursor="hand2",command=update_employee)
update_button.grid(row=0,column=2,pady=5,padx=10)

delete_button=CTkButton(button_frame,text="Delete Employee",font=("arial",18,"bold"),width=160,cursor="hand2",command=delete_employee)
delete_button.grid(row=0,column=3,pady=5,padx=10)

delete_all_button=CTkButton(button_frame,text="Delete All",font=("arial",18,"bold"),width=160,cursor="hand2",command=delete_all)
delete_all_button.grid(row=0,column=4,pady=5,padx=15)


all_employees()

tree.bind("<ButtonRelease>",select_employee)
search_box.bind("<<ComboboxSelected>>",search_input)
window.mainloop()