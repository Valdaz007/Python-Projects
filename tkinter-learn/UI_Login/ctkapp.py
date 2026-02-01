import customtkinter as ctk # type: ignore

root = ctk.CTk()
root.title('MiLoginApp')
root.geometry('750x450')
root.configure(fg_color='aliceblue')

loginFrame = ctk.CTkFrame(root, fg_color='aliceblue')
inp_uname = ctk.CTkEntry(loginFrame, placeholder_text="Username", font=ctk.CTkFont(size=16))
inp_upwd = ctk.CTkEntry(loginFrame, placeholder_text="Password", font=ctk.CTkFont(size=16))

def main():
    loginFrame.place(relx=.5, rely=.5, anchor='center')

    lbl_head = ctk.CTkLabel(loginFrame, 
                            text='Mi Login System',
                            font=ctk.CTkFont(size=28, weight='bold'), text_color='dodgerblue')
    lbl_head.pack()
    inp_uname.pack(fill='x', padx=5, pady=10)
    inp_upwd.pack(fill='x', padx=5, pady=(0, 10))

    btn_login = ctk.CTkButton(loginFrame, text='Login', command=login)
    btn_login.pack(fill='x', padx=5)

def login():
    if(inp_uname.get()=='valdaz' and inp_upwd.get()=='1234'):
        print('Login: Success!')
    else:
        print('Login: Invalid!')

if __name__ == "__main__":
    main()
    root.mainloop()