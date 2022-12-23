person_one= ['soddique',
             'male',
             'bangladesh',
             '24th dec 1988',
             'sidproof@gmail.com',
             '01636360199']

person_two= ['mamun',
             'male',
             'united kingdom',
             '10th dec 1988',
             'mamun@gmail.com',
             '01636360109']

gender= person_one[1]
if gender == 'male':
    relative='his'
    pronoun='he'
else:
    relative='her'
    pronoun='she'

sentence=[f'{person_one[0].title()} born in {person_one[2].title()}. {relative.title()} date of birth {person_one[3]}. {pronoun.title()} available at {person_one[4]} .and {relative.title()} '
          f'phone number is {person_one[5]}']
print(sentence)