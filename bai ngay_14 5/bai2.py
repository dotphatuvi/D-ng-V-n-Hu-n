n = int(input("Nhập n: "))

day_so = []
for i in range(n):
    x = float(input(f"Nhập x[{i+1}]: "))
    day_so.append(x)

phan_tu_am = []
for x in day_so:
    if -1000 < x < -10:
        phan_tu_am.append(x)


if len(phan_tu_am) > 0:
    trung_binh = sum(phan_tu_am) / len(phan_tu_am)
    print(f"Các phần tử thỏa mãn: {phan_tu_am}")
    print(f"Trung bình cộng: {trung_binh:.2f}")
else:
    print("Không có phần tử nào thỏa mãn điều kiện!")