class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance  #__ ->for private
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
    def show_balance(self):
        print("the balance is ",self.__wallet_balance)
    def get_wallet_balane(self):
        return self.__wallet_balance
c1=customer(100,"gopal",24,1000)
#print(c1.__wallet_balance)#give error this line
c1.update_balance(500)
c1.show_balance()
