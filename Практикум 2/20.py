a,b = input()
b = int(b)
if a in 'aceg':
    if b % 2 != 0:
        print('черная')
    else:
        print('белая')
elif a in 'bdfh':
    if b % 2 == 0:
        print('черная')
    else:
        print('белая')