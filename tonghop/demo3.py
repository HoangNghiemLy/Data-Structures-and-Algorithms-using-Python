'''
viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
'Others': Thoát chương trình 
'''
import Rectangle as rect
menu_options ={
    1: "Đọc dữ liệu từ file input.db",
    2: "Thêm mới hình chữ nhật",
    3: "Hiển thị danh sách hình chữ nhật",
    4: "Lưu danh sách hình chữ nhật xuống file demo4output.db",
}
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])
dsHCN = []
while(True):
    print_menu()
    chon = ''
    try:
        chon = int(input("Nhập tùy chọn: "))
    except:
        print("Nhập sai định dạng, hãy nhập lại..")

    if chon == 1:
        #1 - Đọc dữ liệu từ file input.db
        fr = open('input.db',mode='r',encoding='utf-8')
        dsHCN = []
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr,cd)
            dsHCN.append(hcn)
        fr.close()
    elif chon == 2:
        #2 - Thêm mới hình chữ nhật
        cr = float(input("Nhập chiều rộng: "))
        cd = float(input("Nhập chiều dài: "))
        hcn = rect.Rectangle(cr,cd)
        dsHCN.append(hcn)
    elif chon == 3:
        #3 - Hiển thị danh sách hình chữ nhật
        if dsHCN.count == 0:
            print("Danh sách rỗng")
        else:
             for item in dsHCN:
                 item.display()

    elif chon == 4:
        #4 - Lưu danh sách hình chữ nhật xuống file demo4output.db
        fw = open('outputdemo4.db',mode='w',encoding='utf-8')
        for item in dsHCN:
            fw.write(f"{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n)")
        fw.close()
    else:
        print("Thoát chương trình BYE BYE")
        break

