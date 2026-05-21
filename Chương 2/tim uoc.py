n = float(input("Nhap so n: "))
i = 2
dem = 0
while (i < n):
    if (n % i == 0):
        dem = dem + 1
    i = i + 1
print ("So uoc cua n la: ", dem)