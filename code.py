
# s = " gege bbff "  # Входная строка
# r = []  # Список для хранения символов
# number = []
# h = []

# for x in s:
#     r.append(x)
# print(r)

# for i in range(len(r)):
#     if i + 1 < len(r) or i == len(r):
#         n = r[i+1]
#         if r[i] != n:
#             number.append(r[i])
#             print(f"to {number}")
#             if r[-1] == n:
#                 number.append(r[-1])
#                 print(number)
                

# print(f"two {number}")
# # сравнить два списка с начала за условием и выдать результат отфильтрованого
# for _ in range(len(r)):
#     for x in range(len(number)): 
#         if x + 1 < len(number):
#             n = number[x+1]
#             number.sort()
#             if number[x] == n:
#                 print(f"del {number[x]}")
#                 del number[x]
# print(f"3 {number}")
# tetsr = []
# testnumber = []            
# for _ in r:
#     tetsr.append(_)
# for x in number:
#     testnumber.append(x)

# print(tetsr)
# print(testnumber)

# for n in range(len(number)):
#     if n == 0:        
#         h.append(1)
#     h.append(n)

# print(sum(h))

print("New start")
print("")
try:
    s = str(input("abc - "))  # Входная строка 
except: 
    print("Restart")
    s = str(input("abc - "))  # Входная строка abcbdeafg
number = []
h = []
n = -1
for x in s:
    if x in h:
        n +=1
        if n > len(number):
            number.append(h.copy())    
            if n == 2:
                del number[0]
        pipo = h.index(x)
        h = h[pipo+1:]  # Обрезаем список после первого вхождения повторяющегося символа
    h.append(x)

if number == []:
    number.append(h.copy())
max = 0
for i in range(len(number)):
    for x in range(len(number[i])):
        if len(number[i]) > max:
            max = len(number[i])
            max_str = "".join(number[i])
            print(F"Най більши строки - (<{max_str}>) = {max}")
 

