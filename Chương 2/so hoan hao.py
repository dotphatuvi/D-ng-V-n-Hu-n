#Số hoàn hảo là số bằng tổng các số ước của nó 
#vd: 6=1+2+3; 24=1+2+4+7+14
n = int(input("n = "))
s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i
    if s == n:
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")
  