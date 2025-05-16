a = 15 
b = 5 

while a > b:
    if a % 2 == 0:
        b+=a
    else:
        a = a - b * 2 + 1
print(b)