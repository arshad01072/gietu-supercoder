class data:
    def __init__(self):
        self.__s_id=None
        self.__age=None
        self.__marks=None
        self.__cal=None
    def set_s_id(self,s_id):
        self.__s_id=s_id
    def set_age(self,age):
        self.__age=age
    def set_marks(self,marks):
        self.__marks=marks
    def cal(self):
        if self.get_age()>20 and self.get_marks()>0 and self.get_marks()<100:
            if(self.get_marks()>85):
                a=self.get_marks()-self.get_marks()*0.25
                print("ellibile for dicount","student id:",self.get_s_id(),"discount is :",a)
            else:
                print("not get discount")
            if self.get_marks()>65:
                print("ellgible for addmission")
            else:
                print("not elible")
        else:
            print("not ellgible")
    def get_s_id(self):
        return self.__s_id
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def display_details(self):
        print("student id:",self.__s_id,"age:",self.__age,"marks:",self.__marks)
o=data()
o.set_s_id(int(input("enetr the id:")))
o.set_age(int(input("enetr the age")))
o.set_marks(int(input("enetr the marks")))
print("verify for eligibility and discount")
o.display_details()
o.cal()
