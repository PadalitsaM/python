raw = input('Enter number:')
try:
    num = int(raw)
    print(num)
except ValueError:
    print('Please enter a number')