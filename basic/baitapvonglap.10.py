#Viết chương trình tính tổng các số chia hết cho 3 hoặc 5 từ 1 đến n
def tinhTongCacSoChiaHetCho3Hoac5(n):
    tong = 0
    for i in n:
        if i % 3 == 0 or i % 5 == 0:
            tong += i
    return tong

n = int(input("Nhập số n: "))
print(f"Tổng các số chia hết cho 3 hoặc 5 từ 1 đến {n} là {tinhTongCacSoChiaHetCho3Hoac5(range(1,n+1))}")