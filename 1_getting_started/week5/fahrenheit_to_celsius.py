inp=input('enter fahrenheit temprature' )
try:
    fahrenheit=float(inp)
    celcius=(fahrenheit-32)*5/9
    print(celcius)
except:
    print('please enter a number')
