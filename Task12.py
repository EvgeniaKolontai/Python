# Для натурального n создать словарь индекс-значение, 
# # состоящий из элементов последовательности 3n + 1.
a = int(input(' N = '))
dictionary = {}
for i in range(1, a+1):
    dictionary.setdefault(i, 3* i + 1)/
    # dictionary[i] =3* i + 
print(dictionary)
    
dictionary = [i-1 for i in range(10)]
a = 6
dictionary = {n: 3 * n +1 for n in range(1, a+1)}
print(dictionary)

    