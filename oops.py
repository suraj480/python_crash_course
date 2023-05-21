class Employee:
    salary=89
    name="Rohan"
    def getSalary(self):
        return self.salary
rohan=Employee()
print(rohan.salary)
print(rohan.name)

class factoryEmployee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
suraj=factoryEmployee("ritul","1234")
print(suraj.salary)
print(suraj.name)

suraj=factoryEmployee("vivan","123888884")
print(suraj.salary)
print(suraj.name)