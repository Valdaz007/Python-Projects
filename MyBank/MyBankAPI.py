import time

class Account:
    _SeedNum = 1000000000

    def __init__(self, name, initbalance):
        self._transList = []
        self._AcctName = name
        self._Balance = 0
        self._AcctNo = self._SeedNum
        self._SeedNum += 1
        self.Deposit(initbalance)
    
    def __str__(self):
        return f'Account Name: {self.AcctName}\tAccount Number: {self._AcctNo}'
    
    @property
    def Balance(self):
        return f"{self._Balance}"

    @property
    def AcctName(self):
        return f"{self._AcctName}"

    @property
    def AcctNo(self):
        return f"{self._SeedNum}"

    @property
    def TransHist(self):
        return self._transList
            
    @AcctName.setter
    def AcctName(self, name):
        self._AcctName = name
    
    @Balance.setter
    def Balance(self, balance):
        if balance > 0:
            self.AddTransaction(amount, f'Reset Balance')
            self._Balance = balance
    
    def Deposit(self, amount):
        if amount > 0:
            self.AddTransaction(amount, f'Deposit ')
            self._Balance += amount
    
    def Withdraw(self, amount):
        if amount > 0:
            self.AddTransaction(amount, f'Withdraw')
            self._Balance -= amount

    def AddTransaction(self, amount, note):
        date_depo = time.strftime("%e %B, %Y", time.localtime())
        trans = Transaction(amount, date_depo, note)
        self._transList.append(trans)

class Transaction:
    
    def __init__(self, amount, date, note):
        self._amount = amount
        self._date = date
        self._note = note
    
    @property
    def transAmnt(self):
        return f"{self._amount}"

    @property
    def transDate(self):
        return f"{self._date}"

    @property
    def transNote(self):
        return f"{self._note}"
