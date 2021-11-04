class User:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance = self.balance + amount    

    def make_withdrawal(self, amount):
        self.balance = self.balance - amount

    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance = self.balance - amount
        other_user.balance = other_user.balance + amount
        print(f"Transaction completed, {self.name} transfer {amount} to {other_user.name}")
        

luis = User("Luis Galindo", 1000)
cami = User("Camila Galindo", 500)
gianna = User("Gianna Grasso", 2000)

luis.deposit(1000)
luis.deposit(200)
luis.deposit(600)
luis.make_withdrawal(800)
luis.display_user_balance()

cami.deposit(500)
cami.deposit(100)
cami.make_withdrawal(700)
cami.display_user_balance()

gianna.deposit(100)
gianna.make_withdrawal(200)
gianna.make_withdrawal(2000)
gianna.make_withdrawal(100)
gianna.display_user_balance()


luis.transfer_money(cami, 100)
luis.display_user_balance()
cami.display_user_balance()
