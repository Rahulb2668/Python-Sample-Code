person = {'name': 'Rahul', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and i am ' + str(person['age']) + 'years old'
# print(sentence)

# sentence = 'My name is {} and i am {} years old'.format(person['name'], person['age'])
# print(sentence)

sentence = 'My name is {1} and i am {0} years old'.format(person['name'], person['age'])
print(sentence)
sentence = f'{person[name]},{person[age]}'
# #
# tag = 'h1'
# text = 'This is the headline'
#
# sentence = '<{0}> {1} </{0}>'.format(tag, text)
# print(sentence)

# ##
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# #
# p1 = Person('Jack', '33')
# p2 = Person('kiran','98')
# sentence = 'My name is {0.name} and I am {1.age} years old'.format(p1, p2)
#
# print(sentence)

# # Formatting a dictionary
# person_dict = {'name': 'Curly', 'age': '34'}
# sentence = 'My name is {name} and i am {age}'.format(**person_dict)
# print(sentence)

# print(f"My name is {person['name'] } and i am {person['age'] } years old")