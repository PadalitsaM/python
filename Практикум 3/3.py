from math import sqrt
a= int(input('Введите число:'))

while True:
    if sqrt(a) == int(sqrt(a)):
        print(f'Число {a} является полным квадратом')
        break
    else:
        a = int(input('Введите новое число:'))