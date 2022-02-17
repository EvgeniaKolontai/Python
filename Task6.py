# Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным.
import os
def clear(): return os.system('cls')
clear()
day = int(input('--> '))
if day % 7 == 6:
    print('sub')
elif day % 7 == 0:
    print('vsk')
else : 
    print('будний')