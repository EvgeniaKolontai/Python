# Подсчитать сумму цифр в вещественном числе
a = float(input(' Enter num : '))
sum = 0
for i in str(a):
    if i != '.':
        sum += int(i)
print(f' sum = {sum}')

