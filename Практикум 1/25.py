x, y, n = map(int, input().split())
m = (x * 100 + y) * n
r = m // 100
l = m - r * 100
print(f'{r} руб. {l} коп.')