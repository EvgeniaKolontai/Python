# Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти
import os # чистим консоль перед выводом
clear = lambda: os.system('cls')#чистим консоль перед выводом
clear()#чистим консоль перед выводом
a = int(input('Ведите номер четверти: '))
if a == 1 :
    print( " от 0 до +х, +у бесконечности")
if a == 2 :
    print( " от 0 до +х, -у бесконечности")
if a == 3 :
    print( " от 0 до -х, -у бесконечности")  
if a == 4 :
    print( " от 0 до -х, +у бесконечности") 
