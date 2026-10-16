a = int(input())

if a <= 10:
    print(a - 1)
else:
    a -= 10
    if a <= 180:
        index = (a - 1) // 2
        position = (a - 1) % 2
        number = 10 + index
        if position == 0:
            print(number // 10)
        else:
            print(number % 10)
    else:
        a -= 180
        index = (a - 1) // 3
        position = (a - 1) % 3
        number = 100 + index
        if position == 0:
            print(number // 100)
        elif position == 1:
            print((number // 10) % 10)
        else:
            print(number % 10)


