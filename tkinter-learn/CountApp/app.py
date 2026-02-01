import tkinter as tk


def btnCounter():
    counter.set(counter.get()+1)

wdw = tk.Tk()
wdw.title('MiCounterApp')
wdw.geometry('450x300')
wdw.config(bg='#2b2b2b')

counter = tk.IntVar()
counter.set(0)

lbl_counter = tk.Label(wdw, text='0', bg='#2b2b2b', fg='#ffffff', textvariable=counter)
lbl_counter.pack()

btn_counter = tk.Button(wdw, text='Count', bg='#ffa002',
                        command=btnCounter)
btn_counter.pack()

wdw.mainloop()