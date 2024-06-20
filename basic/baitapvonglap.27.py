#Khởi tạo list chứa n giá trị. Không dùng hàm min(), tìm và in ra màn hình giá trị nhỏ nhất trong list
def nhapMang(n):
    list = []
    for i in range(n):
        list.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
    return list
def timSoNhoNhat(list):
    so_nho_nhat = list[0]
    for i in range(1,len(list)):
        if list[i] < so_nho_nhat:
            so_nho_nhat = list[i]
    return so_nho_nhat

def main():
    n = int(input("Nhập số phần tử của list: "))
    list = nhapMang(n)
    print(f"Số nhỏ nhất trong list là {timSoNhoNhat(list)}")
if __name__ == "__main__":
    main()