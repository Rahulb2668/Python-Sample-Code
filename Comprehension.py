nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Making a list using for loop

# my_list = []
# for n in nums:
#     my_list.append(n)
#
# print(my_list)

# # List Comprehension

# my_list = [n for n in nums]
# print(my_list)


# #To make a list of square of numbers

# my_list = [n*n for n in nums]
# print(my_list)


# # using a map and lambda
# # Map is function that through the list using a function and lambda is an anonymous function

# my_list = map(lambda n: n*n, nums)
# print(my_list)


# # Making a list of even numbers

# my_list = []
# for n in nums:
#     if(n%2 == 0):
#         my_list.append(n)
#
# print(my_list)

# In Comprehensions
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)


# # I want a (letter , num) pair for each letter in 'abcd' and each number in '1234'

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# #Comprehension

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)


# # Dictionary Comprehensions

# subjects = ['maths', 'Science', 'Physics', 'Social']
# Marks = ['90', '80', '95', '100']

# my_dict = {}
#
# for subjects, Marks in zip(subjects, Marks):
#     my_dict[subjects] = Marks
# print(my_dict)
#
# my_dict = {subject: Mark for subject, Mark in zip(subjects, Marks)}
# print(my_dict)


# # Set Comprehension
# 
# my_set = set()
# my_set = {n for n in nums}
# print(my_set)