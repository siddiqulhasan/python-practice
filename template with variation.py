import random
person=['siddique','sylhet']
name=person[0]
location=person[1]

sentence_one_group =[f'this is {name}',
                     f'my name is {name}',
                     f'{name} is my name']


sentence_three=[f'I live in {location}',
                f'i reside in {location}',
                f'i was raised in {location}',
                f'{location} is the place where i reside']
sentence_one=random.choice(sentence_one_group)
sentence_three=random.choice(sentence_three)
paragraph=f'{sentence_one} . {sentence_three}'
print(paragraph)