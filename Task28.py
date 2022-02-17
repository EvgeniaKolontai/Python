# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
import math
def squer():  
    # list = {}
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
        # print(f'Enter {a}*x*8**2 + {b}*x + {c}')
    d = b**2 -4*a*c
    x1= 0
    x2 = 0
    if d > 0:
        x1=((-b+(math.sqrt (d))**1/2)/2*a) 
        x2=((-b-(math.sqrt(d))**1/2)/2*a)
        print(f"x1 = %.2f \nx2 = %.2f" % (x1, x2),{d})
    elif d==0 :
        x1 = -b / (2 * a)
        print(f'd=0',{d})
    elif d <0 :
        print(f'Kорней нет, d<0',{d})
        # list.append(x1,x2)
    print(squer(a, b, c))