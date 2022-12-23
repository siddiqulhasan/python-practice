students=[]
while True:
    name=input('enter your name:')
    if name=='shesh':
        print(students)
        print('total students:', len(students))
        break
    else:
        students.append(name)