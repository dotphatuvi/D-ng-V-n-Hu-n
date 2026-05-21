a = float(input("Nhap diem toan\n"))
b = float(input("Nhap diem ly\n"))
c = float(input("Nhap diem hoa\n"))
tb = (a + b + c) / 3
print ("Diem trung binh la: ", tb)
if (tb >= 9):
    print ("Xep loai gioi") 
elif (tb >= 7):
    print ("Xep loai kha")
elif (tb >= 5):
    print ("Xep loai trung binh")           