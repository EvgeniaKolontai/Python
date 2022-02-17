# Определить, присутствует ли в заданном списке строк, некоторое число 

n = int(input("Enter num: "))
list=['12', '15', '165','889','7890']

for i in range(len(list)):
    list[i] = int(list[i])
    if n == list[i]:
        print(f'Yes , индекс числа {i} ')
        break
else :
    print('no')

