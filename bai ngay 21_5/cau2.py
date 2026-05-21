n = int(input("Nhập n: "))

tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10

if tong % 3 == 0:
    print(f"Tổng các chữ số của {n} là {tong} → chia hết cho 3")
else:
    print(f"Tổng các chữ số của {n} là {tong} → không chia hết cho 3")