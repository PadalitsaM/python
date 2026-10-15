a = input()
if len(a) == 4:
    n1,n2,n3,n4 = list(map(int, str(a)))
    if n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4:
        if not 1900 <= int(a) <= 2050:
            print('Ok')
        else:
            print('Error')
    else:
        print('Error')
else:
    print('Error')
