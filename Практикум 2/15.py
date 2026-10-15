n,k,m = map(int,input().split())
if k < m :
    n1 = m - k - 1
    n2 = (k - 1) + (n - m)
    if n1 < n2:
        print(n1)
    else:
        print(n2)
else:
    n1 = k - m - 1
    n2 = (n - k) + (m - 1)
    if n1 < n2:
        print(n1)
    else:
        print(n2)