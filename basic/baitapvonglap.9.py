#Viết chương trình tính tổng các số từ 1 đến n
def tinhTong(n):
    tong = 0
    for i in n:
        tong += i
    return tong

n = int(input("Nhập số n: "))
print(f"Tổng các số từ 1 đến {n} là {tinhTong(range(1,n+1))}")