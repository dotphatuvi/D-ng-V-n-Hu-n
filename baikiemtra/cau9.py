a = int(input("nhap so nguyen a:\n"))
b = int(input("nhap so nguyen b:\n"))
c = int(input("nhap so nguyen c:\n"))

tong = a + b + c
dem = 0

for ch in str(tong):
    if int(ch) % 2 == 0:
        dem = dem + 1

print("tong cua 3 so la", tong)
print("so chu so chan trong tong: ", dem)