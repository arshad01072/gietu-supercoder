class customer:
    def _init_(self):
        self.__quantity=None
    def validate_quantity(self,quantity):
        self.__quantity=quantity
        if self.__quantity>0:
            return True
        else:
            return False
class Pizzaservice:
    def _init_(self):
        self.__pizza_type=None
        self.__quantity=None
        self.__add_toping=None
    def validate_pizza_type(self,pizza_type,quantity,add_toping):
        self.__pizza_type=pizza_type
        self.__quantity=quantity
        self.__add_toping=add_toping
        l=[]
        id=""
        num=100
        if (self.__pizza_type =="Small" or self.__pizza_type=="Medium") :
            a=self.__pizza_type[0]
            if a=='S' or a=='M':
                id=a+str(num)
                self.__quantity_price=150*self.__quantity
                if self.__add_toping >1:
                    self.__quantity_price=self.__quantity_price+self.__add_toping*35
            l.append([id,self.__quantity_price])
            num=num+1
        else:
            l.append([0,0])
        return l

class Door_Deliver:
    def init(self):
        self.__d=None
        self.__pc=None
    def pizza_cost_door(self,dis,pizza_cost):
        self.__d = dis
        self.__pc = pizza_cost
        if(self.__d <6):
            self.__pc=self.__pc+(self.__d*5)
            return self.__pc
        elif(self.__d>=6):
            self.__pc=self.__pc+((self.__d-5)*7)+(self.__d*5)
            return self.__pc




v1=customer()
q=int(input("enter the quantity"))
v1_sol=v1.validate_quantity(q)
print("VERIFY",v1_sol)
if v1_sol==True:
    v2=Pizzaservice()
    v2_sol=v2.validate_pizza_type("Small",q,3)
    print("ID    AND    AMOUNT AFTER TOPING",v2_sol)
else:
    print(-1)
# print(v2_sol[0][1])
distance=int(input("ENTER DISTANCE"))
if v2_sol[0][1]!=0 and distance>1:
    v3=Door_Deliver()
    v3_sol=v3.pizza_cost_door(distance,v2_sol[0][1])
    print("COST OF PIZZA ACCORDING TO DISTANCE",v3_sol)
else:
    print("not valid distance")
