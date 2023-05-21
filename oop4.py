
class BankAccount:
    
    def __init__(self,account_number,balance,dateOo,cname):
        self.account_number=account_number
        self.balance=balance
        self.dateOo=dateOo
        self.cname=cname
        
    def deposit(self,amount):
        self.balance +=amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -=amount
        return self.balance
    
    def check_balance(self):
        return self.balance
    
p1=BankAccount(12,100,'12/5/2021','Maya')
print('Balnce before deposit and withdraw: ',p1.check_balance())
print()
print('Balnce after deposit: ',p1.deposit(1000))
print()
print('Balnce after withdraw: ',p1.withdraw(500))
