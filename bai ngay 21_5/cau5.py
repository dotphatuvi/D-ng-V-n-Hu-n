m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong_chu_so_n = 0
temp = n
while temp > 0:
    tong_chu_so_n += temp % 10
    temp =temp // 10

if m % tong_chu_so_n == 0:
    print(f"Tổng chữ số của {n} = {tong_chu_so_n} → {m} chia hết cho {tong_chu_so_n}")
else:
    print(f"Tổng chữ số của {n} = {tong_chu_so_n} → {m} không chia hết cho {tong_chu_so_n}")