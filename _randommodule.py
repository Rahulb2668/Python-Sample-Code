import random

# vsl = random.random() # gets no between 0 and 1
# print('Random No: '+str(vsl))

# vsl = random.uniform(1, 10) # Between 1 and 10(exclusive)
# print(vsl)

# To get a int

# vsl = random.randint(1, 6) # Both are inclusive
# print(vsl)


# greetings = ['Hello', 'Hi', 'Hola', 'Howdy', 'Good day']

# vsl = random.choice(greetings)
# print(vsl)

# color = ['black', 'green', 'red']
# results = random.choices(color, k=10)  # K represents how many times you have to pick a random value
# print(results)

# We can add weight to the variables

# color = ['black', 'green', 'red']
# results = random.choices(color, weights=[18, 18, 2], k=10)  # K represents how many times you have to pick
# print(results)

# deck = list(range(1, 53))
#
# random.shuffle(deck)  # To shuffle a passed parameter
# print(deck)
#
# # To select a no from the above deck
# # Here we cannot use choices method because it may choose the same card more than one time
#
# hand = random.sample(deck, k=5)  # it chooses the unique values each time
# print(hand)


