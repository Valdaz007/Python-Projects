from MyBankAPI import Account

def main():
    acct1 = Account('Victor', 1000)
    acct2 = Account('Ezy', 200)
    
    acct1.Deposit(200)
    acct1.Withdraw(500)

    print(str(acct1))
    for trans in acct1.TransHist:
        print(f'{trans.transNote}\t\t{trans.transAmnt}\t{trans.transDate}')
    
    acct1.AcctName = 'Arnold'

    print(str(acct1))
    
    
if __name__ == "__main__":
    main()