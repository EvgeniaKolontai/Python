# Найти расстояние между двумя точками пространства

def find_lenth ():
    string = input('Введите координаты точки F, B х,у  через запятую: ')
    a = string.split(',')
    for i in range(len(a)): 
        a[i] = int(a[i])
    return a
x = find_lenth()
y = find_lenth()
print(x)
print(y)
distance = ((x[0]-y[0])**2) + ((x[1]-y[1])**2)
print(distance)