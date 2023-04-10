class LimitReachedException(Exception):
    "Your Account Limit has Reached"
    pass

class OverDrawException(Exception):
    "You are Overdrawing"
    pass

class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance
        
    def get_account_type(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance
    
    def set_balance(self,balance):
        self.__balance = balance

class Customer(Account,PriviledgeCustomer):
    def __init__(self,customer_id, customer_name, age,account_type,balance,min_balance,bonus_points=None):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__age = age
        Account.__init__(self,account_type,balance,min_balance)
        PriviledgeCustomer.__init__(self,bonus_points,balance)
        
    def withdraw(self,amount):
        try:
            if super().get_balance() < super().get_min_balance():
                raise LimitReachedException
            elif amount>super().get_balance():
                raise OverDrawException
            else:
                if super().getbonuspoints()==None:
                    pass
                else:
                    super().increase_bonus()
                super().set_balance(super().get_balance()-amount)
        except OverDrawException:
            print("You are OverDrawing")
        except LimitReachedException:
            print("Account Limit Reached")
    
    def take_card():
        return "Take out the card"
    
    def get_customer_id(self):
        return self.__customer_id
    
    def get_customer_name(self):
        return self.__customer_name
    
    def get_age(self):
        return self.__age

class PriviledgeCustomer:
    def __init__(self,bonus_points,balance):
        self.__bonus_points = bonus_points
        self.__balance = balance    
        
    def getbonuspoints(self):
        return self.__bonus_points
    
    
    def increase_bonus(self):
        if self.__balance>1000:
            self.__bonus_points+=10
        else:
            self.__bonus_points+=2

C = Customer(100,'Gopal',43,'Savings',1000,500,100)
C.withdraw(100)
C.withdraw(500)
C.withdraw(100)
print(C.get_balance())
print(C.getbonuspoints())
