count=0
total=0
print('before', count,total)
for numbers in [9,41,12,3,74,15]:
    count=count+1
    total=total+numbers
    print (count,total,numbers)
print('After', count, total, total/count)
