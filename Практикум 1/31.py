x, y = map(int, input().split())
res = (x % y) * (y % x) + 1
print(res)