"""
 'istitle( ), isypper( ), islower( ), isspace( ), 'isidentifier( )', 'encode'

"""

str1 = "PYTHON!"
str2='i love phython'
str3='I love Phython'
str4=' '
str5='siddiqulHasan'
str6='7hasan'
str7 ='Ståle'
print(str1.istitle())
print(str2.islower())
print(str4.isspace())
print(str5.isidentifier(),str6.isidentifier())
print(str7.isidentifier())
print('normal print:', str7)
print('encoded print:', str7.encode())