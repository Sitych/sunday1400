from random import randint

a = int(input())
b = int(input())
n = int(input("кол-во чисел в списке: ")) #в условии не было про сказано про размер списка, так что добавил от себя
l = []

while a <= n:
    l.append(randint(a,b))
    a += 1
print(l)

l2 = []
for i in range(len(l)):
    if i % 2 == 0:
        l2.append(l[i])
print(l2)
    

 

