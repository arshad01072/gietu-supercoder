class Employee:
    def __init__(self):
        self.employee_id=None
    def check_eligiblity(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("the employee is eligible for special benifits")
        else:
            print("the employee is not eliginke for special beenifits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligiblity()
emp2=Employee()
emp2.employee_id=9100
emp2.check_eligiblity()
