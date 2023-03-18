class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("total price of",self.brand,"mobile is",self.total_price)
    def amnt_return(self):
        return (self.price-self.total_price)
mob1=mobile("apple",2000)
mob2=mobile("sumsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amnt_return())
print(mob2.amnt_return())
