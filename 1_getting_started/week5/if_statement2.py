sh=input('enter hours')
sr=input('enter rate')
fh=float(sh)
fr=float(sr)
#print(fh,fr)
if fh > 40:
    print('overtime')
    regular=fh*fr
    otp=(fh-40.0)*(fr*0.5)
    xp=regular+otp
else:
    xp=fh*fr
print ('pay',xp)
