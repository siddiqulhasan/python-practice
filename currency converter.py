#usd= '95'
#print(usd, type(usd))

#usd = 95
#print(usd, type(usd))

#usd= int('95')
#print(usd, type(usd))

usd= input('enter your usd amount:')
usd= float(usd)
exchange_rate= 100
bdt=usd * exchange_rate
#print(usd,'is equl to', bdt , 'bdt')

paragraph = str(usd) +'is equal to'+ str(bdt) +'bdt'

print (paragraph)
