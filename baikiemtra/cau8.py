x = int(input("nhap so nguyen x:\n"))
y = int(input("nhap so nguyen y:\n"))
z = int(input("nhap so nguyen z:\n"))

tich = x * y * z
chu_so = str(tich)
so_chu_so = len(chu_so)
chu_so_lon_nhat = max(chu_so)

print("tich cua 3 so la: ", tich)
print("so chu so la: ", so_chu_so)
print("chu so lon nhat la: ", chu_so_lon_nhat)