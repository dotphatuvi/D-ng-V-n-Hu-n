n = int(input("Nhập n: "))

tich = 1
temp = n
while temp > 0:
    tich *= temp % 10
    temp //= 10

if tich % 2 == 0 and tich > 20:
    print(f"Tích các chữ số của {n} là {tich} → là số chẵn và lớn hơn 20 ✅")
else:
    print(f"Tích các chữ số của {n} là {tich} → không thỏa mãn ❌")