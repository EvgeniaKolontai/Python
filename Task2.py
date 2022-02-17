# Найти максимальное из пяти чисел
import os # чистим консоль перед выводом
clear = lambda: os.system('cls')#чистим консоль перед выводом
clear()#чистим консоль перед выводом
x = [2,4,6,8,1220,20,40,142,145,475,695]
v = max([el for el in x if el > 0 and el <475])
v1 = min ([el for el in x if el > 0 and el < 40])
print(v, v1)



    


