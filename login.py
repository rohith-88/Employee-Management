from tkinter import messagebox
from customtkinter import *
from PIL import Image


def login():
  if username_entry.get()== "" or password_entry.get()=="":
    messagebox.showerror("Error","All fields required!")

  elif username_entry.get()== "admin" or password_entry.get()=="123":
    messagebox.showinfo("Success","Login Successful")
    root.destroy()
    import management
  else:
    messagebox.showerror("Error","Not authorized")


root = CTk()

root.geometry("1200x700")
root.resizable(0,0)
root.title("Login")

image=CTkImage(Image.open("./imgs/loginpage.png"),size=(1200,900))
image_label=CTkLabel(root,image=image,text="")
image_label.place(x=0,y=-100)

header=CTkLabel(root,text="Employee Management System",bg_color="#FFFFFF",font=("Arial",30,"bold"))
header.place(x=60,y=150)

# usernameField=CTkEntry(root,placeholder_text="Enter username")
# usernameField.place(x=200,y=250)

username_label = CTkLabel(root, text="Username",bg_color="#FFFFFF",font=("Arial",20,"bold"))
username_label.place(x=180,y=250)
username_entry = CTkEntry(root,bg_color="#FFFFFF",font=("Arial",20,"bold"),width=200)
username_entry.place(x=180,y=290)


password_label = CTkLabel(root, text="Password",bg_color="#FFFFFF",font=("Arial",20,"bold"))
password_label.place(x=180,y=360)
password_entry =CTkEntry(root, show="*",bg_color="#FFFFFF",font=("Arial",20,"bold"),width=200)
password_entry.place(x=180,y=400)

login_button = CTkButton(root, text="Login",font=("Arial",20,"bold"),width=200,bg_color="#FFFFFF",fg_color="#fbc63d",text_color="#FFFFFF",cursor="hand2",command=login)
login_button.place(x=180,y=470)

root.mainloop()