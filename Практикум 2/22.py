n,k,m = map(int,input().split())
if n <= k:
    time = 2 * m
if (2 * n) % k == 0:
    time = (2 * n // k) * m
else:
    time = (2 * n // k) * m + m
print(time)