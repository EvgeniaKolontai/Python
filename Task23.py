# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
def count():
    list = [5, 2, 3, 4, 6, 1, 7]
    list2 = []
    res = 0
    print(list)
    for i in range(len(list)// 2+1):
        res = list[i]*list[len(list) - 1 - i]
        if i < len(list)/2:
            list2.append(res)    
    print(list2)

count()

# import math

# def index_mult(list1,list2):
#     for i in range(0,math.ceil(len(list1)/2)):
#         first = list1[i]
#         last = list1[len(list1)-1-i]
#         mult = first * last
#         list2.append(mult)
#     print(list2)


# listF = [2,3,4,5,6]
# newF = []
# listS= [2, 3, 5, 6]
# newS = []

# index_mult(listF, newF)
# index_mult(listS, newS)
