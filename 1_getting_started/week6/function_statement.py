def computepay(hours,rate):
    #print ("in computepay")
    if hours > 40:
        regular=hours*rate
        otp=(hours-40.0)*(rate*0.5)
        pay=regular+otp
    else:
        pay=(hours*rate)

    #print ('pay')
    return pay

sh=input('enter hours')
sr=input('enter rate')
fh=float(sh)
fr=float(sr)
#print(fh,fr)

xp=computepay(fh,fr)
print("pay",xp)
