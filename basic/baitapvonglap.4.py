#Hãy nhập từ bàn phím số tự nhiên n và xuất ra màn hình:
#a. Các số nguyên tố nhỏ hơn n 
#b. Xuất ra tổng các số nguyên tố nhỏ hơn n

def kiemTraSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True

def soNguyenToNhoHonN(n):
    for i in range(2,n):
        if kiemTraSoNguyenTo(i):
            print(i, end=" ")
    print()

def tinhTongCacSoNguyenTo(n):
    s = 0
    for i in range(2,n):
        if kiemTraSoNguyenTo(i):
            s+=i
    return s
def main():
    n = int(input("Nhập n: "))
    print(f"Các số nguyên tố nhỏ hơn {n} là: ")
    soNguyenToNhoHonN(n)
    print(f"Tổng các số nguyên tố nhỏ hơn {n} là {tinhTongCacSoNguyenTo(n)}")
if __name__ == "__main__":
    main()


