number = int(input('Enter value: '))
for i in range(number):
    for j in range(i+1):
        print('*', end="")
    print()
