# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
def statement_truth(a,b):
    if (not (a or b)) == ((not a) and (not b)):
        print(f'True for: x = {a}, y = {b}')
    else:
        result = False
        print(result)

result = True

x = True
y = True

statement_truth(x,y)

x = True
y = False

statement_truth(x,y)


x = False
y = True

statement_truth(x,y)

x = False
y = False

statement_truth(x,y)
