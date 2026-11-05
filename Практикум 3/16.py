n = int(input())

for num in range(2, n + 1):
    summa = 0
    for d in range(1, num):
        if num % d == 0:
            summa += d
    if summa == num:
        print(num)