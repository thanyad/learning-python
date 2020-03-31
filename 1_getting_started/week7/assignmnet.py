largest=None
smallest=None
while True:
        number=input("Enter a number:")
        if number == "done":
            break
        try:
            number=int(number)
            if largest == None:
                largest  = number
            elif largest < number:
                largest = number

            if smallest==None:
                smallest=number
            elif smallest>number:
                smallest=number

        except ValueError:
            print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)
