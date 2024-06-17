#Bank
class Bank_Account:
    def __init__(self,customer_name,balance,account_number):
        self.customer_name=customer_name
        self.balance=balance
        self.account_number=account_number
    def __str__(self):
        return self.customer_name

customer1=Bank_Account("Siva",10000,24335355)
print(customer1.customer_name,customer1.balance,customer1.account_number)
print(customer1)