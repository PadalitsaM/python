a = input()
num1,num2 = a.split(':')
if int(num1) > int(num2):
    print('1')
elif int(num1) < int(num2):
    print('2')
elif int(num1) == int(num2):
    print('0')
else:
    print('Ошибка')
