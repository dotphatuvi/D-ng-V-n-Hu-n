n = int(input("Nhập n: "))
day_so = []
for i in range(n):
    x = float(input(f"Nhập x[{i+1}]: "))
    day_so.append(x)

phan_tu_duong = [x for x in day_so if 0 < x < 1000]

if len(phan_tu_duong) > 0:
    tb = sum(phan_tu_duong) / len(phan_tu_duong)
    print(f"Trung bình cộng: {tb:.2f}")
else:
    print("Không có phần tử nào thỏa mãn!")