n, k, r = map(int, input().split())
d = 1
while n < r:
    n = n + (1 / 100) * k * n
    d += 1
print(d)