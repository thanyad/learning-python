data='from stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008'
first=data.find('@')
#print(first)

next=data.find(' ',first)
#print(next)

host=data[first+1 : next]
print(host)
