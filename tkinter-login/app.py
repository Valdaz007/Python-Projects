import tkinter as tk

wdw = tk.Tk()

wdw.title('MiLogin')
wdw.geometry('340x440')
wdw.configure(bg="#2B2B2B")


lbl_intro = tk.Label(wdw, text='Mi Login', bg='#2b2b2b', fg="#ffa200", 
                     font=('Roboto', 20))

lbl_uname = tk.Label(wdw, text='Username', bg='#2b2b2b', fg='#f3f3f3',
                     font=('Roboto', 16))
lbl_upwd = tk.Label(wdw, text='Password', bg='#2b2b2b', fg='#f3f3f3',
                    font=('Roboto', 16))

inp_uname = tk.Entry(wdw, font=('Roboto', 16))
inp_upwd = tk.Entry(wdw, show="*", font=('Roboto', 16))

btn_login = tk.Button(wdw, text='Login', bg='#ffa200', font=('Roboto', 12))

# Placing Widgets
lbl_intro.grid(row=0, column=0, columnspan=2, pady=10)
lbl_uname.grid(row=1, column=0, pady=5)
lbl_upwd.grid(row=2, column=0, pady=5)

inp_uname.grid(row=1, column=1)
inp_upwd.grid(row=2, column=1)

btn_login.grid(row=3, column=0, columnspan=2, pady=10)

wdw.mainloop()