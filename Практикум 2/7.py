a = int(input())
d1 = a // 1000
d2 = (a // 100) % 10
d3 = (a // 10) % 10
d4 = a % 10
if d1 == d4 and d2 == d3:
    print('настоящее')
else:
    print('кривое')