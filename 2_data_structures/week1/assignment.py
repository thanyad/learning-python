str = "X-DSPAM-Confidence:    0.8475"
first=str.find(':')
print(first)
piece= str[first+2:]
#print(piece)
piece.strip()
#print(piece)
value= float(piece)
print(value)
