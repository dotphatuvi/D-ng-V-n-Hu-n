n=int(input("nhap n:"))
while n>200 or n <= 0:
    n=int(input("nhap n (0<n<200)"))
a=[]
for i in range (n):
    x=int(input(f"nhap so thu {i+1}:"))
    a.append(x)
tong=0
for i in a:
    if i%2==0:
        tong +=i
print ("tong chan =",tong)
if tong%7==0 and tong<200:
    print("tong chia het cho 7 va nho hon 200")
else:
    print("tong khong chia het cho 7 hoac lon hon 200")