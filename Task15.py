# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
n=int(input( 'Enter N : '))
list = list(range(1, n+1))
print(list , end= ' --->')
f = 1
list1=[]
for i in list:
    f *= i+1
    list1.append(f)
print(list1)
       