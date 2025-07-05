import tkinter as tk
import Bank_operations as acc

window=tk.Tk()
window.title("Welcome Sbi Bank")
window.geometry("500x400")

def accountFun():
    acc.create_account()

def loginFun():
    acc.login_user()

def deleteFun():
    acc.delete_acc()

def funClose():
    window.destroy()

title=tk.Label(window,text="Welcome to SBI Bank",font=("Arial",17),bg="aqua",fg="black")
account=tk.Button(window,text="Create Account",width=13,font=("Arial",12),bg="blue",fg="white",command=accountFun)
login=tk.Button(window,text="Login Account",width=13,font=("Arial",12),bg="blue",fg="white",command=loginFun)
delete=tk.Button(window,text="Delete existing account",width=20,font=("Arial",12),bg="blue",fg="white",command=deleteFun)
close=tk.Button(window,text="close",width=13,command=funClose,bg="red",fg="white",font=("Arial",12))

title.place(x=150,y=20)
account.place(x=200,y=100)
login.place(x=200,y=140)
delete.place(x=200,y=180)
close.place(x=200,y=250)

window.mainloop()