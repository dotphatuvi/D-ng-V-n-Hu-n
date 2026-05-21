a = []
s = 0
n = int(input("nhap so phan tu cua day so: "))
for i in range(1, n + 1):
    x = int(input("nhap phan tu thu " + str(i) + ": "))
    a.append(x)
    s += x
print("tong cac phan tu trong day so la: " + str(s))
for i in range(n):
   s = i**2
print("binh phuong cua " + str(i) + " la: " + str(s))