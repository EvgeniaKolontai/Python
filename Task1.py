# По двум заданным числам проверить является ли одно квадратом второго 
print('Введите а');
a = int(input())
print('Введите b');
b = int(input())
if (a == b * b):
    print('Первое число квадрат второго')
elif a != b * b :
    print('Первой чиcло не квадрат второго')
