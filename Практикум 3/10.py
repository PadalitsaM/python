n = float(input())
count = 0
while n !=0:
    k = float(input())
    if k == 0:
        break
    if k < n:
        count += 1
    n = k
print(count)