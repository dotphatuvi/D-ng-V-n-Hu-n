a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

tong = a + b
chu_so_lon_nhat = max(int(c) for c in str(tong))

print(f"Tổng a + b = {tong}")
print(f"Chữ số lớn nhất trong {tong} là: {chu_so_lon_nhat}")