#Khởi tạo list chứa n giá trị. Không dùng hàm max(), tìm và in ra màn hình giá trị lớn nhất trong list

def nhapMang(n):
    list = []
    for i in range(n):
        list.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
    return list
def timSoLonNhat(list):
    so_lon_nhat = list[0]
    for i in range(1,len(list)):
        if list[i] > so_lon_nhat:
            so_lon_nhat = list[i]
    return so_lon_nhat

def main():
    n = int(input("Nhập số phần tử của list: "))
    list = nhapMang(n)
    print(f"Số lớn nhất trong list là {timSoLonNhat(list)}")
if __name__ == "__main__":
    main()
