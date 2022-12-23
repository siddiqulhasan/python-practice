#number= int(input('enter number'))

#if number == 0:
    #print(number, 'is zero')
#elif number % 2 == 0:
    #print(number, 'is even number')
#lse:
   # print(number, 'is odd number')

#number=int(input('enter number'))
#if number >= 80:
    #print( 'A+')
#elif number >= 70:
    #print('A')
#elif number >= 60:
    #print('A-')
#elif number >= 50:
    #print('B')
#else:
   # print('Unsuccessful Attempt')

number= int(input('enter number'))

if number % 2 == 0:
    if number == 0:
        print(number, 'is zero')
    else:
        print(number, 'is even')
else:
    print(number, 'is odd')
