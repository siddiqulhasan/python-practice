years=[1988, 1999,2080,2090,2085]
i=0
while i < len(years):
    if years[i] % 4 == 0:
        print(years[i], 'is leap years')
    i = i+1