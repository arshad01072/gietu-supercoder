class shoe:
     def __init__(self,price,material):
        self.price=price
        self.material=material
     def __str__(self):
         return "shoe with price:"+str(self.price)+"and material:"+self.material
s1=shoe(1000,"canvas")
print(s1)

