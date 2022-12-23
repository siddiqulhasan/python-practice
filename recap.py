
gender = input('enter gender (male/femail):')
if gender == 'male':
    profession = 'actor '
    pronoun = 'he'
    relative= 'him'
else:
    profession = 'actress'
    pronoun = 'she'
    relative = 'her'

print(f'{pronoun} is an {profession} . i know {relative}')