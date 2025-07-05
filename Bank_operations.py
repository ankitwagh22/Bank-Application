import tkinter as tk
import tkinter.messagebox as msg
import random
import mysql.connector as msq

conn=msq.connect(database="bank",user="root",password="12345678")
cur=conn.cursor()

def create_account():
    wind=tk.Tk()
    wind.title("Create Your Account")
    wind.geometry("500x400")

    page_title=tk.Label(wind,text="Create Your SBI Saving Account",font=("Arial",14),bg="blue",fg="white")
    fname_label=tk.Label(wind,text="first Name",font=("Arial",12),fg="blue")
    lname_label = tk.Label(wind, text="Last Name", font=("Arial", 12),fg="blue")
    un_label=tk.Label(wind,text="Create Username", font=("Arial", 12),fg="blue")
    passwd_label=tk.Label(wind,text="Create password",font=("Arial",12),fg="blue")
    city_label=tk.Label(wind,text="Enter Your City",font=("Arial",12),fg="blue")

    first_name=tk.Entry(wind,width=14,font=("Arial",12))
    last_name=tk.Entry(wind, width=14, font=("Arial", 12))
    username=tk.Entry(wind,width=14, font=("Arial", 12))
    passwd=tk.Entry(wind,width=14, font=("Arial", 12))
    city=tk.Entry(wind,width=14, font=("Arial", 12))


    def submit():
        if len(first_name.get()) != 0 and len(last_name.get()) != 0 and len(username.get()) != 0 and len(
                passwd.get()) != 0 and len(city.get()) != 0:

            # Generating random account number
            nums = [i for i in range(1, 10)]
            acc_no = ''
            for i in range(6):
                acc_no += str(random.choice(nums))
            acc_no = int(acc_no)

            cmd = "insert into sbi_bank values (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(cmd, params=[str(first_name.get()), str(last_name.get()),acc_no,str(username.get()), str(passwd.get()), str(city.get()),0])
            if cur.rowcount==1:
                conn.commit()
                msg.showinfo(title="Account information", message="Account Successfully created..")
            else:
                msg.showerror(title="Error",message="Technical issue")
        else:
            msg.showerror(title="error",message="All fields are compalsory to fill")

    first_name.delete(0,tk.END)
    last_name.delete(0,tk.END)
    username.delete(0,tk.END)
    passwd.delete(0,tk.END)
    city.delete(0,tk.END)

    def closeFun():
        wind.destroy()

    # Submit button
    button=tk.Button(wind,text="Submit",width=10,font=("Arial",12),bg="blue",fg="white",command=submit)
    # close button
    close=tk.Button(wind,text="close",width=10,font=("Arial",12),bg="red",fg="white",command=closeFun)

    page_title.place(x=120,y=20)
    fname_label.place(x=120,y=90)
    first_name.place(x=250,y=90)
    lname_label.place(x=120,y=120)
    last_name.place(x=250,y=120)
    un_label.place(x=120,y=150)
    username.place(x=250,y=150)
    passwd_label.place(x=120,y=180)
    passwd.place(x=250,y=180)
    city_label.place(x=120,y=210)
    city.place(x=250,y=210)
    button.place(x=150,y=250)
    close.place(x=260,y=250)
    wind.mainloop()
    conn.close()

def delete_acc():
    window=tk.Tk()
    window.title("Delete Account")
    window.geometry("500x400")

    accNum_label=tk.Label(window,text="Enter Your Account Number -->",font=("Arial",15))
    accNum=tk.Entry(window,width=17,font=("Arial",14),fg="green")

    def delete():
        acc_no=accNum.get()
        cur.execute("delete from sbi_bank where acc_no=%s",params=[acc_no])
        if cur.rowcount==1:
            conn.commit()
            msg.showinfo(title="Account delete",message="Account Delete Successfully!")
        else:
            msg.showerror(title="Error",message="Invalid Account Number")
        accNum.delete(0,tk.END)

    def close():
        window.destroy()

    # submit button
    submit=tk.Button(window,width=10,font=("Arial",11),fg="white",bg="purple",text="delete",command=delete)
    # close button
    cls=tk.Button(window,width=10,font=("Arial",11),fg="white",bg="red",text="close",command=close)

    accNum_label.place(x=100,y=30)
    accNum.place(x=150,y=80)
    submit.place(x=120,y=130)
    cls.place(x=250,y=130)

    window.mainloop()
    conn.close()

def login_user():
    root=tk.Tk()
    root.title("Login Your account")
    root.geometry("500x400")

    title=tk.Label(root,text="Login Your Account",font=("Arial",18),fg="blue")
    username_label=tk.Label(root,text="Username",font=("Arial",15))
    passwd_label=tk.Label(root,text="Password",font=("Arial",15))
    username=tk.Entry(root,width=15,font=("Arial",15),fg="green")
    passwd=tk.Entry(root,width=15,font=("Arial",15),fg="green")

    def submit():
        uname=username.get()
        pwd=passwd.get()
        cur.execute("select * from sbi_bank where username=%s and password=%s",params=[uname,pwd])
        data=cur.fetchone()
        if cur.rowcount==1:
            conn.commit()
        if data==None:
            msg.showerror(title="error",message="username,password not entered !")
        print(data)

        username.delete(0,tk.END)
        passwd.delete(0,tk.END)

    def closeFun():
        root.destroy()

    # submit button
    sub_btn=tk.Button(root,text="Submit",width=14,font=("Arial",12),bg="blue",fg="white",command=submit)
    # close window button
    close_btn=tk.Button(root,text="Close",width=14,font=("Arial",12),bg="red",fg="white",command=closeFun)

    title.place(x=140,y=30)
    username_label.place(x=100,y=100)
    username.place(x=210,y=100)
    passwd_label.place(x=100,y=140)
    passwd.place(x=210,y=140)
    sub_btn.place(x=120,y=200)
    close_btn.place(x=280,y=200)

    root.mainloop()