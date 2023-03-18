class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)
print("the unique id of the object",id(s1))
