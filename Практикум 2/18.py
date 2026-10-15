a,b = map(int, input().split('x'))
c,d,e = map(int, input().split('x'))
k = a * b
s1 = c * d
s2 = c * e
s3 = d * e
if s1 < k or s2 < k or s3 < k:
    print('Да')
else:
    print('Нет')