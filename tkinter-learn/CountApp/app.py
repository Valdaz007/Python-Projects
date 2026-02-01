import tkinter as tk

wdw = tk.Tk()
wdw.title('MiCounterApp')
wdw.geometry('450x300')
wdw.config(bg='#2b2b2b')

counter = tk.IntVar()
counter.set(0)

def btnCounter():
    counter.set(counter.get()+1)

def main():

    # Define Window Grid
    wdw.columnconfigure(0, weight=1, uniform='grp1')
    wdw.columnconfigure(1, weight=1, uniform='grp1')
    wdw.rowconfigure(0, weight=1)

    pnl1 = tk.Frame(wdw, bg='dodgerblue')
    pnl2 = tk.Frame(wdw, bg='aliceblue')
    pnl1.grid(row=0, column=0, sticky='news')
    pnl2.grid(row=0, column=1, sticky='news')

    lbl_Head = tk.Label(pnl1, bg='dodgerblue', fg='white', text='The Most\n Awsome \nCounter App', font=('Roboto', 20), pady=60)
    lbl_Head.pack()

    pnl2Cont = tk.Frame(pnl2, bg='aliceblue')
    pnl2Cont.pack(pady=50)

    lbl_counter = tk.Label(pnl2Cont, text='0', bg='aliceblue', fg='black', font=('Roboto', 12), textvariable=counter)
    btn_counter = tk.Button(pnl2Cont, text='Count', bg='#ffa002', command=btnCounter)
    lbl_counter.pack()
    btn_counter.pack(pady=10)

    wdw.mainloop()

if __name__ == "__main__":
    main()