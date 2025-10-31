class BankAccount :
  def __init__(self,balance):
    self.balance = balance

  def deposit(self,amount):
    if (amount <= 0) :
      print("Deposit have to be greater than zero ")
    else:
      pass