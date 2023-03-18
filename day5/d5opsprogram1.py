class vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__vehicle_premium=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        if vehicle_type=="two wheeler" or vehicle_type=="four wheeler":
            self.__vehicle_type=vehicle_type
        else:
            return "invalid vehicle name given"
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_vehicle_premium(self,vehicle_premium):
        self.__vehicle_premium=vehcile_premium
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def calculate_premium(self):
        if self.__vehicle_type=="two wheeler":
            self.__vehicle_premium=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="four wheeler":
            self.__vehicle_premium=self.__vehicle_cost*0.06
    def get_vehicle_premium(self):
        return self.__vehicle_premium
    def display_vehicle_details(self):
        print("vehicle id:",self.__vehicle_id,"vehicle typr:",self.__vehicle_type,"vehicle cost:",self.__vehicle_cost,"vehicle premium:",int(self.__vehicle_premium))
v1=vehicle()
v1.set_vehicle_id(int(input("enter the vehicle id")))
v1.set_vehicle_type(input("enetr the vehicle type"))
v1.set_vehicle_cost(int(input("enter the vehcile cost")))
v1.calculate_premium()
print("vehcile details:")
v1.display_vehicle_details()
                    
        
