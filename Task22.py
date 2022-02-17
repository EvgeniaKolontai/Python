# Найти сумму чисел списка стоящих на нечетной позиции
n = int(input('-->'))
mylist = list(range(n))

print(mylist)

sum = 0

for i in range(0,len(mylist)-1):
    if i % 2 == 1:
        sum += mylist[i]
        
print(sum)

 
