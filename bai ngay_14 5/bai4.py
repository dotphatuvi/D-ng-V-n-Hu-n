m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = m + n

chu_so_lon_nhat = 0
temp = tong
while temp > 0:
    chu_so = temp % 10
    if chu_so > chu_so_lon_nhat:
        chu_so_lon_nhat = chu_so
    temp= temp// 10

print(f"Tổng m + n = {tong}")
print(f"Chữ số lớn nhất trong {tong} là: {chu_so_lon_nhat}")