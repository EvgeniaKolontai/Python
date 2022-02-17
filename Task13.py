# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# str1 = input('Enter firtht string ')
# # str2 = input('Enter second string ')
# str1 = 'GeeksforGeeks'
# str2 = 'ks'
# res = ""
# for i in str1:
#      if i in str2 and not i in res:
#          res += i
# print ("String intersection is : " + res)
# res = set(str1).intersection(str2)
# print ("String intersection is : " + str(res))

a = '123 два три раз два три'
b = 'раз'

flag = True
c = 0
while flag :
    now_index = a.find(b)
    if now_index != -1 :
        a = b[now_index + len(b):]
        c+=1
    else:
        print(c)
        flag = False

