#students=['rony', 'jamal', 'kamal', 'robiul']
#students.append('badhaha')
#students.insert(1,'rabbi')
#students[1:3]=['aminul', 'fokrul']
#students=' **** '.join(students)
#students.sort(reverse=True)
#print(students)

numbers=[21,25,23,27,29,31,33,35,39]
i=0
while i < len(numbers):
    if numbers[i] % 3 == 0:
        print(numbers[i], ' odd numbers')
    i=i+1