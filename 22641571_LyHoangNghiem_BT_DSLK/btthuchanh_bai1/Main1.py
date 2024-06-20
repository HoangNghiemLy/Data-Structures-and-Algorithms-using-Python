'''
hãy viết menu cho chương trình quản lý danh sách liên kết
thêm lệnh xóa màn hình
1. Thêm phần tử ( cho người dùng nhập số lượng phần tử cần thêm)
2. In danh sách
3. Số lượng các phần tử
4. Tổng giá trị các phần tử
5. Giá trị lớn nhất
6. Giá trị nhỏ nhất
7. Sắp xếp tăng dần
8. Sắp xếp giảm dần
9. Danh sách các số chẵn
10. In danh sách theo thứ tự ngược
11. Thoát


'''
import os 
from DSLK import DSLK
ds = DSLK()
while True:
    
    os.system('cls')
    print("===Menu===")
    print("1. Thêm phần tử")
    print("2. In danh sách")
    print("3. Số lượng các phần tử")
    print("4. Tổng giá trị các phần tử")
    print("5. Giá trị lớn nhất")
    print("6. Giá trị nhỏ nhất")
    print("7. Sắp xếp tăng dần")
    print("8. Sắp xếp giảm dần")
    print("9. Danh sách các số chẵn")
    print("10. In danh sách theo thứ tự ngược")
    print("11. Thoát")
    chon = int(input("Mời bạn chọn: "))
    if chon == 1:
        n = int(input("Nhập số lượng phần tử cần thêm: "))
        for i in range(n):
            x = int(input("Nhập giá trị cần thêm: "))
            ds.them(x)

        

    elif chon == 2:
        ds.in_ds()
    elif chon == 3:
        print("Số lượng các phần tử: ",ds.soluongcacphantu())
    elif chon == 4:
        print("Tổng giá trị các phần tử: ",ds.tonggiatri())
    elif chon == 5:
        print("Giá trị lớn nhất: ",ds.giatri_max())
    elif chon == 6:
        print("Giá trị nhỏ nhất: ",ds.giatri_min())
    elif chon == 7:
        ds.sapxep_tang()
        ds.in_ds()
    elif chon == 8:
        ds.sapxep_giam()
        ds.in_ds()
    elif chon == 9:
        ds.ds_chan()
    elif chon == 10:
        ds.in_ds_nguoc()
    else:
        break
    input("Nhấn phím bất kỳ để tiếp tục")

    
print("Cảm ơn bạn đã sử dụng chương trình")


 