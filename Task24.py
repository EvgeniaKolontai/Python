# В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
def find():
    sourcelist = [1.1, 1.2, 3.1, 5, 10.01]
    intlist = []
    fraclist = []
    frac = 0
    for i in range(0,len(sourcelist)):
        frac = round((sourcelist[i] - math.floor(sourcelist[i])),3)
        if frac==0:
            pass
        else:
            fraclist.append(frac)
    print(max(fraclist)-min(fraclist))

find()