import tkinter as tk

wdw = tk.Tk()
wdw.title('MiCounterApp')
wdw.geometry('450x300')
wdw.config(bg='#2b2b2b')

lbl_counter = tk.Label(wdw, text='0', bg='#2b2b2b', fg='#ffffff')
lbl_counter.pack()

btn_counter = tk.Button(wdw, text='Count', bg='#ffa002')
btn_counter.pack()

wdw.mainloop()