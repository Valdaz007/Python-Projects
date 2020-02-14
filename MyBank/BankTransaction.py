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
