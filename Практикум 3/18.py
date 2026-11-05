x = int(input())
count = 0

for a in range(1, int(x ** 0.5) + 1):
    for b in range(a, int(x ** 0.5) + 1):
        if a ** 2  + b ** 2 == x:
            count += 1

print(count)