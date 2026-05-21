a = float(input("nhap so thu nhat = "))
b = float(input("nhap so thu hai= "))
c = float(input("nhap so thu ba= "))
max = a
if(b > max):
    max = b
if(c > max):
    max = c
print("so lon nhat trong ba so %f, %f, %f la: %f" % (a, b, c, max))