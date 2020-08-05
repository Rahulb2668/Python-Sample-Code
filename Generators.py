# # using list
#
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
#
#
# print(square_numbers([1, 2, 3, 4, 5]))


# # Generators

#
# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
#
# my_nums = square_numbers([1, 2, 3, 4, 5])
#
# # print(my_nums)
# # They yield one result at a time
#
# # print(next(my_nums))
#
# # Or U can use a for loop
# for num in my_nums:
#     print(num)

# replace [] in list comprehension with () then its generator
# my_nums = (x*x for x in [1, 2, 3, 4, 5])

# print(my_nums)
# print(list(my_nums)) # Not a good method because it looses its advantages
# for num in my_nums:
#     print(num)


# Generators are very much good in performance. Because they don't hold values in memory
