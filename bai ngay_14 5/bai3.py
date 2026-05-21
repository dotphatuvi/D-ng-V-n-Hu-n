a = int(input("Nhập a: "))
b = int(input("Nhập b: "))


chu_so_nho_nhat = 9
temp = b
while temp > 0:
    chu_so = temp % 10
    if chu_so < chu_so_nho_nhat:
        chu_so_nho_nhat = chu_so
    temp =temp// 10

if chu_so_nho_nhat == 0:
    print("Chữ số nhỏ nhất là 0, không thể chia cho 0!")
elif a % chu_so_nho_nhat == 0:
    print(f"Chữ số nhỏ nhất của {b} là {chu_so_nho_nhat},{a} chia hết cho {chu_so_nho_nhat}")
else:
    print(f"Chữ số nhỏ nhất của {b} là {chu_so_nho_nhat},{a} không chia hết cho {chu_so_nho_nhat}")