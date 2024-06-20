#viết menu cho chương trình quản lý danh sách liên kết
#thêm lệnh xóa màn hình

# '''

import os
from bt2 import DSLK2
ds = DSLK2()

while True:
    os.system('cls')
    print("===Menu===")
    print("0. Thêm phần tử vào danh sách")
    print("1. Thêm pt vào cuối ds")
    print("2. Thêm 1 pt vào trước pt nào đó")
    print("3. In ds")
    print("4. In ds theo thứ tự ngược")
    print("5. Tìm GTNN, GTLN trong ds")
    print("6. Tính tổng số âm, tổng số dương trong ds")
    print("7. Tính tích các số trong ds")
    print("8. Tính tổng bình phương của các số trong ds")
    print("9. Nhập x, xuất các số là số nguyên tố của x")
    print("10.Nhập x, xuất các số là ước số của x")
    print("11.Nhập x, tìm giá trị đầu tiên trong ds mà >x.")
    print("12.Xuất số nguyên tố cuối cùng trong ds")
    print("13.Đếm các số nguyên tố")
    print("14.Kiểm tra xem ds có phải đã được sắp tăng không")
    print("15.Kiểm tra xem ds có các pt đối xứng nhau hay không")
    print("16.Xóa pt cuối")
    print("17.Xóa pt đầu")
    print("18.Hủy toàn bộ ds")
    print("19. Thoát")
    chon = int(input("Mời bạn chọn: "))
    if chon == 0:
        n = int(input("Nhập số lượng phần tử cần thêm: "))
        for i in range(n):
            x = int(input("Nhập giá trị cần thêm: "))
            ds.them(x)
    elif chon == 1:
        x = int(input("Nhập giá trị cần thêm: "))
        ds.them_cuoi(x)

    elif chon == 2:
        x = int(input("Nhập giá trị cần thêm: "))
        y = int(input("Nhập giá trị trước pt cần thêm: "))
        ds.them_truoc(x,y)
        
    elif chon == 3:
        ds.in_ds()
    elif chon == 4:
        ds.in_ds_nguoc()
    elif chon == 5:
        print("Giá trị nhỏ nhất: ",ds.gtnn())
        print("Giá trị lớn nhất: ",ds.gtln())
    elif chon == 6:
        print("Tổng số âm: ",ds.tong_so_am())
        print("Tổng số dương: ",ds.tong_so_duong())
    elif chon == 7:
        print("Tích các số: ",ds.tich())
    elif chon == 8:
        print("Tổng bình phương: ",ds.tong_binh_phuong())
    elif chon == 9:
        x = int(input("Nhập x: "))
        ds.so_nguyen_to(x)
    elif chon == 10:
        x = int(input("Nhập x: "))
        ds.uoc_so(x)
    elif chon == 11:
        x = int(input("Nhập x: "))
        print("Giá trị đầu tiên lớn hơn x: ",ds.gt_dau_tien_lon_hon_x(x))
    elif chon == 12:
        print("Số nguyên tố cuối cùng: ",ds.so_nguyen_to_cuoi_cung())
        
    elif chon == 13:
        print("Số lượng số nguyên tố: ",ds.dem_so_nguyen_to())
        
    elif chon == 14:
        if ds.kiem_tra_sap_xep_tang() == True:
            print("Danh sách đã được sắp xếp tăng")
        else:
            print("Danh sách chưa được sắp xếp tăng")
        
    elif chon == 15:
        if ds.kiem_tra_doi_xung() == True:
            print("Danh sách có các pt đối xứng nhau")
        else:
            print("Danh sách không có các pt đối xứng nhau")
        
    elif chon == 16:
        ds.xoa_cuoi()
    elif chon == 17:
        ds.xoa_dau()
    elif chon == 18:
        ds.huy_toan_bo()
    else:
        break
    input("Nhấn Enter để tiếp tục...")
print("Cảm ơn bạn đã sử dụng chương trình!")



    

        