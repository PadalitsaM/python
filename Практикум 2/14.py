a = int(input())
gall = 17 * 29
if a // gall > 0:
    print(f'{a // gall} галлеонов')
    a -= (a // gall) * gall
    if a // 29 > 0:
        print(f'{a//29} сиклей')
    else:
        print(f'{a} кнатов')

else:
    if a > 29:
        print(f'{a//29} сиклей')
        a -= (a // 29) * 29
        if a >0 :
            print(f'{a} кнатов')
    else:
        print(f'{a} кнатов')