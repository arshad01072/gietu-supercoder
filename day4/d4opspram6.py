class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
#mobile().purchase()        
        
m1=mobile()
print(m1)
m2=mobile()
print(m2)
m1=m2
print(m1)
print(m2)
