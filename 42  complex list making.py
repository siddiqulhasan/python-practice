
person= [['soddique','male','bangladesh', '24th dec 1988', 'sidproof@gmail.com', '01636360199'],
         ['samawat', 'femail',  'united kingdom', '10th dec 1988','mamun@gmail.com', '01636360109'],
         ['fawzan', 'male',  'canada', '10th dec 2000','fawzan@gmail.com', '01636365109'],
         ['jakwan', 'male',  'united states', '25th dec 1988','jakwan@gmail.com', '01676360109']

         ]
i=0
while i <len(person):
  single_person=person[i]
  name= single_person[0]
  gender=single_person[1]
  country=single_person[2]
  birthdate=single_person[3]
  email_address=single_person[4]
  phone_number=single_person[5]
  if gender == 'male':
      pronoun= 'he'
      relative='his'
  else:
      pronoun='she'
      relative='her'

  sentence=f'{name} lives in {country} . {pronoun} was born in {birthdate}.{relative} email address {email_address}'
  print(sentence)
  i=i+1
  #print(name,gender,country,birthdate,email_address,phone_number, sep='------')
