#Dùng for...in:
#a. Liệt kê danh sách các ký tự có trong 1 từ, với từ được nhập vào từ bàn phím
#b. Liệt kê danh sách các giá trị có trong 1 danh sách, với danh sách được nhập từ bàn phím

def lietKeKyTu(tu):
    for i in tu:
        print(i, end=" ")
    print()

def lietKeGiaTri(danhSach):
    for i in danhSach:
        print(i, end=" ")
    print()

def main():
    tu = input("Nhập từ: ")
    print("Các ký tự trong từ là: ", end="")
    lietKeKyTu(tu)
    danhSach = input("Nhập danh sách: ").split()
    print("Các giá trị trong danh sách là: ", end="")
    lietKeGiaTri(danhSach)

if __name__ == '__main__':
    main()
    