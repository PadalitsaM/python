from math import ceil
n = int(input())
s = int(input())
num = int(input())
page = n * s
if num % page == 0:
    page_num = num // page
    num_st = s
    num_str = n
else:
    page_num = ceil(num / page)
    num_st = ceil((num % page) / n)
    num_str = ceil((num % page) % n)

print(f'странца {page_num} столбец {num_st} строка {num_str}')