def giai_thua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt