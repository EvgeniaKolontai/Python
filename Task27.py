# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
a = '13 2 455 10123 67 1123 876 23 54'
a = a.split()
b = []
for i in a:
    b.append(int(i))
print(b)
print(f'Max is {max(b)}')
print(f'Min is {min(b)}')

