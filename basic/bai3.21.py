#In ra màn hình các số chẵn của 1 mảng được nhập từ bàn phím
def inCacSoChanTrongMang(mang):
    for i in mang:
        if i%2 == 0:
            print(i,end=" ")
    print()
def nhapMang():
    n = int(input("Nhập số phần tử của mảng: "))
    mang = []
    for i in range(n):
        mang.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
    return mang
def xuatMang(mang):
    for i in mang:
        print(i,end=" ")
    print()
def main():
    mang = nhapMang()
    print("Mảng vừa nhập là: ",end="")
    xuatMang(mang)
    print("Các số chẵn trong mảng là: ",end="")
    inCacSoChanTrongMang(mang)
if __name__ == '__main__':
    main()

