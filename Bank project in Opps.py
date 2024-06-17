#Bank
class Bank_Account:
    customer_name=""
    balance=0.0
    account_number=0

customer1=Bank_Account()
customer2=Bank_Account()

customer1.customer_name="Siva"
customer1.balance=1000
customer1.account_number=123

customer2.customer_name="Gopal"
customer2.balance=2000
customer2.account_number=12345

print(customer1.customer_name)
print(customer2.customer_name)