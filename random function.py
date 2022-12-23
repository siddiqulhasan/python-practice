import random
ludu=[1,2,3,4,5,6]
random_numbers= random.choice(ludu)
if random_numbers == 6:
    print('lucky', 'you have own the match ')
else:
    print(random_numbers, 'is not 6')
#print(random_numbers)