x,y = input().split('-')
a1 = x[0]
b1 = int(x[1])
a2 = y[0]
b2 = int(y[1])
c = "abcdefgh".index(a1) + 1
d = "abcdefgh".index(a2) + 1
let = abs(c-d)
dght = abs(b1-b2)
if (let == 2 and dght == 1) or (let == 1 and dght == 2):
    print('верно')
else:
    print('ошибка')