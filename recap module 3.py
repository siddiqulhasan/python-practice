salary= int(input('enter salary:'))
years_of_services= float(input('enter years of services:'))
if years_of_services > 5 or salary>= 20000:
    bonus = 0.05
    net_salary = salary + salary * bonus
    print('salary including bonus', net_salary, 'USD')
else:
    print('you got basic salary', salary, 'USD')