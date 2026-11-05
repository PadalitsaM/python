n = int(input())
maximum = n
while n != -1:
    if n > maximum:
        maximum = n
    n = int(input())
print(maximum)