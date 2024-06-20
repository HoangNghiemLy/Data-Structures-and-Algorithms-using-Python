#Chương trình menu
#1 - Thêm mới hình tròn
#2 - Hiển thị danh sách hình chữ nhật
#3 - Tính tổng diện tích các hình tròn
#4 - Hiển thị các hình tròn có chu vi nhỏ nhất
#Others: thoát chương trình
import HinhTron as cir
menu_options ={
    1: "Thêm mới hình tròn",
    2: "Hiển thị danh sách hình tròn",
    3: "Tính tổng diện tích các hình tròn",
    4: "Hiển thị các hình tròn có chu vi nhỏ nhất",
    'Others': "Thoát chương trình"
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])
dsHT = []
while(True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input("Nhập lựa chọn: "))
    except:
        print("Nhập sai định dạng, hãy nhập lại...")
        continue
    if userChoice == 1:
        r = float(input("Nhập bán kính: "))
        ht = cir.Circle(r)
        dsHT.append(ht)
    elif userChoice == 2:
        for item in dsHT:
            item.display()
    elif userChoice == 3:
        dienTich = 0.0
        for item in dsHT:
            dienTich += item.area()
            print(f'Tổng diện tích các hình tròn là: {dienTich:.2f}')
    elif userChoice == 4:
        if dsHT.count == 0:
            print("Danh sách rỗng")
        else:
            mincv = dsHT[0].perimeter()
        for item in dsHT:
            if mincv >item.perimeter():
                mincv = item.perimeter()
                print(f'Hình tròn có chu vi nhỏ nhất: {mincv: .2f}')
        for item in dsHT:
            if item.perimeter() == mincv:
                item.display()
    else:
         print("Thoát chương trình BYE BYE")
         break

