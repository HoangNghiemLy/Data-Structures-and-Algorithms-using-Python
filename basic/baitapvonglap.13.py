#Viết chương trình tìm tất cả các số nguyên tố từ 1 đến n
def kiemTraSoNguyenTo(n):
    if n < 2 :
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
    
def cacSoNguyenToTu1DenN(n):
    for i in range(1,n+1):
        if kiemTraSoNguyenTo(i):
            print(i,end=" ")
    print()

def main():
    n = int(input("Nhập n: "))
    print(f"Các số nguyên tố từ 1 đến {n} là: ")
    cacSoNguyenToTu1DenN(n)
if __name__ == "__main__":
    main()
