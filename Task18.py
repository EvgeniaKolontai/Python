# Реализовать алгоритм перемешивания списка.
# import random
# list = list(range(9))
# random.shuffle(list)
# print(list)


# from random import shuffle
# list = list(range(9))
# shuffle(list)
# print(list)
import random
n = int(input('->'))
list = list(range(n))
for i in range(0,len(list)-1):
    j = random.randint(0,len(list)-1)
    list[i], list[j] =  list[j],list[i]

print(list)

