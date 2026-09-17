att = float(input())
comp = float(input())
yds = float(input())
td = float(input())
int = float(input())
a = (comp/att - 0.3) * 5
b = (yds / att - 3) * 0.25
c = (td/ att) * 20
d = 2.375 - (int / att) * 25
rating = ((a + b + c + d)/6) * 100
print(rating)