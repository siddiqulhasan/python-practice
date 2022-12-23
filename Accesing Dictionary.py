user= {'id':1,
       'first_name': 'siddik',
       'last_name': 'chy',
       'user_name':'tutul',
       'password':'123',
       'role':'admin',
}

#first_name = user.get('first_name')
#last_name = user.get('last_name')
#user_name = user.get('user_name')
#password = user.get('password')
#print(first_name, last_name, user_name, password )

keys = user.keys()
values = user.values()
print(list(keys))
print(list(values))