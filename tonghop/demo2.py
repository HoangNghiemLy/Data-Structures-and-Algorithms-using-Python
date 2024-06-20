#Chương trình menu
#1 - Thêm mới hình chữ nhật
#2 - Hiển thị danh sách hình chữ nhật
#3 - Tính tổng diện tích các hình chữ nhật
#4 - Hiển thị các hình chữ nhật có chu vi nhỏ nhất
#Others: thoát chương trình
import Rectangle as rect
menu_options = {
    1: "Thêm mới hình chữ nhật",
    2: "Hiển thị danh sách hình chữ nhật",
    3: "Tính tổng diện tích các hình chữ nhật",
    4: "Hiển thị các hình chữ nhật có chu vi nhỏ nhất",
    'Others': "Thoát chương trình"
}
def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

#khai báo biến lưu trữ những hình chữ nhật
dsHCN = []
while(True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input("Mời bạn chọn: "))
    except:
        print("Nhập sai định dạng, hãy nhập lại....")
        continue
    #Check what choice was entered and act accordingly
    if userChoice == 1:
        cr = float(input("Nhập chiều rộng: "))
        cd = float(input("Nhập chiều dài: "))

        hcn = rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
    elif userChoice == 2:
        for item in dsHCN:
            item.display()
    elif userChoice == 3:
        dientich = 0.0
        for item in dsHCN:
            dientich += item.area()
        print(f"Tổng diện tích các hình chữ nhật là: {dientich:.2f}")
    elif userChoice == 4:
        if dsHCN.count == 0:
            print("Danh sách rỗng")
        else:
             mincv = dsHCN[0].perimeter()
        for item in dsHCN:
            if mincv > item.perimeter():
                mincv = item.perimeter()
        print(f"Các hình chữ nhật có chu vi nhỏ nhất là: ")
        for item in dsHCN:
            if item.perimeter() == mincv:
                item.display()

       
    else:
        print("Thoát chương trình BYE BYE")
        break


