a,b = sorted(map(int, input().split('x')))
c,d,e = sorted(map(int, input().split('x')))
if c <= a and (d <= b or e <= b):
    print('Да')
else:
    print('Нет')