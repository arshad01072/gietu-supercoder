class Example:
    def _init_(self,num1):
        self.num=num1
    def set_num(self,num2):
        self.num=num2
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.get_num(30)
print(obj.get_num())
