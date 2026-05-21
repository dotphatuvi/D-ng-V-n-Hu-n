i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue   # bỏ qua số chẵn, quay lại đầu vòng lặp
    print(i)
    i += 1