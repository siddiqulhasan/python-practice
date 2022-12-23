#print('i\'m gong to make tutorial')
#number=5
#correct_number=int(input('enter correct_number:'))
#if correct_number==number:
   # print('perfect, you are wright!')
#elif correct_number > number:
   # print('we have already received your answer')
#else:
  #  print('no, you are wrong')
number= 5
guess=int(input('enter number'))

if guess!=number:
    if guess>number:
        print('you have entered larger number')
    else:
        print('you have entered smaller number')
else:
    print('you have own the game!')