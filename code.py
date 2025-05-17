
s = " gege bbff "  # Входная строка
r = []  # Список для хранения символов
number = []
h = []

for x in s:
    r.append(x)
print(r)

for i in range(len(r)):
    if i + 1 < len(r) or i == len(r):
        n = r[i+1]
        if r[i] != n:
            number.append(r[i])
            print(f"to {number}")
            if r[-1] == n:
                number.append(r[-1])
                print(number)
                

print(f"two {number}")
# сравнить два списка с начала за условием и выдать результат отфильтрованого
for x in range(len(number)): 
    number.sort()
    print(f"to {x}")
    if x + 1 < len(number):
        n = number[x+1]
        print(f"var - {n}")
        if number[x] == n:
            print(f"del {number[x]}")
            del number[x]
r.sort()            
for _ in number:
    for x in 
    if _ == 
print(number)
# for n in range(len(number)):
#     if n == 0:        
#         h.append(1)
#     h.append(n)

# print(sum(h))
