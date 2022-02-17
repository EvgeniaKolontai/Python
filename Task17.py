# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt   
# в одной строке одно число


# input("Enter list size: ")
import linecache
from random import randint


n = int(input("Enter size of list: "))
list=[]
for i in range(1, n+1):
    list.append(randint( -n, n+1))
new_list =[]
print(list)
index = open ('number_list.txt', 'w') 
index.write('2\n')
index.write('3\n')
path ="number_list.txt"
index = open(path, 'r+')