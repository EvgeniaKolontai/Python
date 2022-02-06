# Найти максимальное из пяти чисел
import os # чистим консоль перед выводом
clear = lambda: os.system('cls')#чистим консоль перед выводом
clear()#чистим консоль перед выводом
x = [2,4,6,8,1220,20,40,142,323,5790,58798765]
v = max([el for el in x if el > 0 and el < 142])
v1 = min ([el for el in x if el > 0 and el < 142])
print(v, v1)

    


