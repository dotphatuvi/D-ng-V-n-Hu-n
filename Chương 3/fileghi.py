n = int(input("Nhap n: "))
a = []
for i in range(n):
    x = int(input("Nhap so: "))
    a.append(x)
open = 0
for i in a:
    while open < n:
        print(a[open])