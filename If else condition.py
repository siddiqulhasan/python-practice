#normal_body_temp = 98.6
#temp= float(input('enter your body temperature'))
#if temp > normal_body_temp:
    #print('paracetamol 2 bela ')
#else:
    #print('vitamin tablet 3 bela')

   # siddique is an actor of bangleshe . he is actor
   #sharmin is an actress of bangladesh . she is actress

name= input('enter name:')
gender = input('enter gender (male/femail):')
country= input('enter country name:')
if gender == 'male':
    profession = 'actor '
    pronoun = 'he'
    known_as = 'nayok'

else:
    profession = 'actress'
    pronoun = 'she'
    known_as = 'naika'

print(f'{name} is an {profession} of {country} . {pronoun} is {known_as} ')