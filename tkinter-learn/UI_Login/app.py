import tkinter as tk
from tkinter import messagebox as msgbox

def btnLogin():
    if(inp_uname.get()=='valdaz' and inp_upwd.get()=='1234'):
        msgbox.showinfo(title='Login Validation', message='Login Successful')
    else:        
        msgbox.showerror(title='Login Validation', message='Login Invalid')


wdw = tk.Tk()

wdw.title('MiLogin')
wdw.geometry('340x440')
wdw.configure(bg="#2B2B2B")

cont = tk.Frame(wdw, bg="#2b2b2b")
cont.pack()

lbl_intro = tk.Label(cont, text='Mi Login', bg='#2b2b2b', fg="#ffa200", 
                     font=('Roboto', 20))

lbl_uname = tk.Label(cont, text='Username', bg='#2b2b2b', fg='#f3f3f3',
                     font=('Roboto', 16))
lbl_upwd = tk.Label(cont, text='Password', bg='#2b2b2b', fg='#f3f3f3',
                    font=('Roboto', 16))

inp_uname = tk.Entry(cont, font=('Roboto', 16))
inp_upwd = tk.Entry(cont, show="*", font=('Roboto', 16))

btn_login = tk.Button(cont, text='Login', bg='#ffa200', font=('Roboto', 12),
                        command=btnLogin)

# Placing Widgets
lbl_intro.grid(row=0, column=0, columnspan=2, pady=10)
lbl_uname.grid(row=1, column=0, pady=5)
lbl_upwd.grid(row=2, column=0, pady=5)

inp_uname.grid(row=1, column=1)
inp_upwd.grid(row=2, column=1)

btn_login.grid(row=3, column=0, columnspan=2, pady=10)

wdw.mainloop()