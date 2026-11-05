n = int(input())
summa= 0

for i in range(n + 1):
    for k in range(i, n + 1):
        summa+= i + k
print(summa)