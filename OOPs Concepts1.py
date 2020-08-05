class Employee:

#     num_of_employees = 0
#     raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
#
#         Employee.num_of_employees +=1
#

    def fullname(self):  # Its a regular Method it takes instance automatically as first argument
        return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod  # Decorator used to make a method take class as the first argument
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#
# #  2 Declaring using init method
#

emp_1 = Employee('Tony', 'Stark', 50000)
emp_2 = Employee('John', 'smith', 10000)

# emp_1 = Employee()

# 1 Declaring the instances directly
# emp_1.first = 'Tony'
# emp_1.last = 'Stark'
#
# print(emp_1.fullname())
# print(emp_2.email)


#  We can also call the function using Class name
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
# print(Employee.num_of_employees)
# Employee.set_raise_amount(1.06)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
