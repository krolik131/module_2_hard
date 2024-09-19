import random
def random_number():
     numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
     random_selection = random.choice(numbers)
     return random_selection
n = random_number()

spisok_par = []
print('В первом поле камня число: ', n)
for i in range(3, n+1):
    if n % i == 0: #целочисленный делитель
        spisok_par.append(i)



x=0
i=0
spisok_parol = []
for i in range(len(spisok_par)):
    x = spisok_par[i]
    for j in range(1,x-i):
        if j + (x - j) == x and j != x / 2:
            spisok_parol.append(j)
            spisok_parol.append(x-j)


result = []
for i in range(0, len(spisok_parol), 2):
    result.append(spisok_parol[i:i + 2])


result1=[]

for i in range(0,len(result)):
    result1 = sorted(result[i])
    result[i] = result1
#print(result)

result.sort(key=lambda x: x[0])
#print(result)

dublicat = []
for i in result:
  if i not in dublicat:
    dublicat.append(i)

print('Пароль для этого числа:')
for i in range(len(dublicat)):
    for j in range(len(dublicat[i])):
        print(dublicat[i][j], end = '')
