#user_1 = {'username':'mamun',
       #   'password': '12345',
          #'role':'admin',
 #}

#user_2=\
#{'username':'sid',
     #   'password': '1245',
      #  'role':'writer',
# }

users = [{'username':'mamun',
          'password': '12345',
          'role':'admin',
},

         {'username':'sid',
        'password': '1245',
        'role':'writer',


        }

         ]

for user in users:
    print(user.get('username'))
    print(user.get('password'))
    print(user.get('role'))