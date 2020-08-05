# li = [9, 1, 2, 3, 4, 5, 8, 6, 7, 0]

# s_li = sorted(li)  # Returns a new sorted list
# print('Sorted new list:', s_li)
# print('Original list:', li)
#
# li.sort()  # sorts the list and returns none
# print('Original list sorted using sort method: ', li)


# # Ascending
#
# s_li = sorted(li, reverse=True)
# print('Printing ascending:', s_li)
#
# # li.sort(reverse = True)
#
# tup = (1, 3, 5, 2, 4, 6, 9, 8, 7)
# # tup.sort() doesn't exist
#
# s_tup = sorted(tup)
# print('Sorted tuple is:', s_tup)

# # Sorting based on absolute value
# li = [-6, -5, -4, 2, 1, 3]
# s_li = sorted(li, key=abs)
# print(s_li)
#

# from operator import attrgetter

# class Employee:
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def __repr__(self):
#         return '{}, {}, ${}'.format(self.name, self.age, self.salary)
#
#
# e1 = Employee('Vishwa', 24, 10000)
# e2 = Employee('Meena', 26, 80000)
# e3 = Employee('Pranam', 40, 70000)
#
# employees = [e1, e2, e3]
#
#
# def e_sort(emp):
#     return emp.name
#
#
# s_employees = sorted(employees, key=e_sort)  # You are just refering the e_sort function not calling it
# #s_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
# #s_employees = sorted(employees, key=attrgetter('age'))
# print(s_employees)
#
