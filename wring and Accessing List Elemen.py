user_one=['sid', 32, 'true','sylhet',]
#print(user_one[0], user_one[-4], sep=' --------* ')
#print(user_one[1], user_one[-3], sep=' ********* ')
#print(user_one[2], user_one[-2], sep=' $$$$$$$$$$ ')
#print(user_one[3], user_one[-1], sep=' @@@@@@@@@@ ')
#partial_list= user_one[1:]
#print(partial_list)


name = user_one[0]
age= user_one[1]
living_place=user_one[3]
is_male=user_one[2]
if is_male:
    pronoun='he'
    gender='man'
else:
    pronoun='she'
    gender='women'
sentence= f'{name} is a {gender} of {age} years old. {pronoun} lives in {living_place}'
print(sentence)