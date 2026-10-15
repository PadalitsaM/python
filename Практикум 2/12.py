a = int(input())
if 11 <= a <= 19:
    print(f'{a} попугаев')
else:
    if a % 10 == 1:
        print(f'{a} попугай')
    elif 2 <= a % 10 <= 4:
        print(f'{a} попугая')
    elif 5 <= a % 10 <= 9 or a % 10 == 0:
        print(f'{a} попугаев')