# # n = 5 
# # lambda x: (-3) ** x)(x) for x in range(n)
# # with open('number_txt.txt', 'a') as data:
# #     data.write(f'{n}\n')

# n = 3
# with open('number_list.txt', 'a', n) as data:
#    for e in range(0, 10):
#         data.write(f'{n * -3}\n')
#         n = n * (-3)
# 
# Определить, позицию второго вхождения
# строки в списке либо сообщить, что её нет.

list = ['qwe', 'asd', 'zxc', 'qwe', 'asd']
x = "qwe"
c = 0

for i in range(len(list)):
   if list[i]== x:
      c+=1
   if c == 2:
      print(i)
      break



