#Viết chuong trình tìm tất cả các ước số của một số nguyên dương n
def uocSo(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i,end=" ")
    print()
def main():
    n = int(input("Nhập n: "))
    print(f"Các ước số của {n} là: ")
    uocSo(n)
if __name__ == "__main__":
    main()
    