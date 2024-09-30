# ## Exercise: Class and Objects

# 1. Create a sample class named Employee with two attributes id and name 

# ```
# employee :
#     id
#     name
# ```


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def display_employee(self):
        print(f'ID: {self.id} \nName: {self.name}')

emp = Employee(1, "Ofgeha")

emp.display_employee()
# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")