
# print('Число Фибоначчи под вашим номером: ', fnum2)
# def fib(n):
#     if n == 1:
#         return 0
#     elif n==2:
#         return 1
#     return fib(n-1) + fib(n-2)
# for i in range(1, 10):
#     print(fib(i), end =" ")

# a1 = 0
# a2 = 1
# k = 8
# for i in range(0, k):
#     a3 = a1 - a2
#     print(a3, end=" ,")
#     a1, a2 = a2, a3

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 2) - fib(n - 1)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)
