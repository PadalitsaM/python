from math import sqrt
r = 6.5
a,b = map(int, input().split('x'))
d = sqrt(a ** 2 + b ** 2)
d2 = 2 * r
if d <= d2:
    print('да')
else:
    print('нет')