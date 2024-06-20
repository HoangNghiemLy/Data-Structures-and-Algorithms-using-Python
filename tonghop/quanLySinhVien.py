import os

class HocSinh:
    def __init__(self, ma_sv, ho_ten, diem, mon_hoc):
        self.__ma_sv = ma_sv
        self.__ho_ten = ho_ten
        self.__diem = diem
        self.__mon_hoc = mon_hoc

    def get_ma_sv(self):
        return self.__ma_sv

    def set_ma_sv(self, ma_sv):
        self.__ma_sv = ma_sv

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, ho_ten):
        self.__ho_ten = ho_ten

    def get_diem(self):
        return self.__diem

    def set_diem(self, diem):
        self.__diem = diem

    def get_mon_hoc(self):
        return self.__mon_hoc

    def set_mon_hoc(self, mon_hoc):
        self.__mon_hoc = mon_hoc

    def to_string(self):
        return f"Ma SV: {self.__ma_sv}, Ho Ten: {self.__ho_ten}, Diem: {self.__diem}, Mon Hoc: {self.__mon_hoc}"

class NODE:
    def __init__(self, data):
        self.data = data
        self.pNext = None

pHead = None

class Linked_List:

    # 1. Chèn một học sinh mới vào danh sách cuối cùng.
    def themSinhVien(x):
        global pHead
        if pHead is None:
            pHead = NODE(x)
        else:
            tmp = pHead
            while tmp != None:
                if tmp.pNext is None:
                    tmp.pNext = NODE(x)
                    break
                tmp = tmp.pNext
                
    #2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm
    def sap_xep_theo_diem():
        global pHead
        tmp = pHead
        while tmp != None:
            tmp1 = tmp.pNext
            while tmp1 != None:
                if tmp1.data.get_diem() < tmp.data.get_diem():
                    tmp1.data, tmp.data = tmp.data, tmp1.data
                tmp1=tmp1.pNext
            tmp = tmp.pNext

    #3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp
    def kiem_Tra_Tang_Dan():
        tmp = pHead
        while tmp != None:
            if tmp.pNext != None and tmp.data.get_diem() > tmp.pNext.data.get_diem():
                return False
            tmp = tmp.pNext
        return True
    
    def chen_hoc_sinh_vao_ds_dasx(k):
        global pHead
        if Linked_List.kiem_Tra_Tang_Dan() == False:
            print("Danh sách ch được sắp xếp")
        else:
            tmp = pHead
            while tmp != None:
                if (k.get_diem() >= tmp.data.get_diem() and tmp.pNext == None) or (k.get_diem() >= tmp.data.get_diem() and k.get_diem() < tmp.pNext.data.get_diem() ):
                    k1 = NODE(k)
                    k1.pNext = tmp.pNext
                    tmp.pNext = k1
                    break
                elif(k.get_diem() < pHead.data.get_diem()):
                    k1 = NODE(k)
                    k1.pNext = pHead
                    pHead = k1
                    break
                tmp = tmp.pNext
            print("Chèn thành công <3")

    #4. Lấy danh sách sinh viên có Điểm lớn hơn x.
    def lay_ds_sv_diem_lon_hon_x(diem1):
        tmp = pHead
        dem = 0
        while tmp is not None:
            if tmp.data.get_diem() > diem1:
                dem+=1
                print(tmp.data.to_string())
            tmp=tmp.pNext
        if dem==0: print("Không có học sinh nào !!!")

    #5. Tìm kiếm k sinh viên có Điểm cao nhất
    def tim_kiem_sinh_vien_diem_cao_nhat():
        max = pHead.data.get_diem()
        tmp = pHead
        while tmp!=None:
            if tmp.data.get_diem()>max: max = tmp.data.get_diem()
            tmp = tmp.pNext
        tmp = pHead
        while tmp!=None:
            if tmp.data.get_diem()==max: print(tmp.data.to_string())
            tmp = tmp.pNext

    #6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x
    def loai_bo_sinh_vien_diem_nho_hon_x(x):
        global pHead
        if pHead ==None:
            return
        
        while pHead.data.get_diem() < x:
            tmp = pHead
            pHead = pHead.pNext
            del tmp
        
        tmp1 = pHead
        while tmp1 !=None:
            while tmp1.pNext != None and tmp1.pNext.data.get_diem() < x:
                huy = tmp1.pNext
                tmp1.pNext = huy.pNext
                del huy
            tmp1=tmp1.pNext

    #7. In sinh viên ra file
    def inThongTinRaFile():
        fr = open("FileThongTin.txt", mode='w', encoding='utf-8')
        tmo = pHead
        while tmo != None:
            fr.write(str(tmo.data.get_ma_sv()) + "," + str(tmo.data.get_ho_ten()) + "," + str(tmo.data.get_diem()) + "," + str(tmo.data.get_mon_hoc()) + "\n")
            tmo = tmo.pNext

    #in danh sachs
    def in_DS():
        tmp = pHead
        while tmp != None:
            print(tmp.data.to_string())
            tmp = tmp.pNext
# Linked_List()

kh9 = HocSinh(1,"Along",1,"ừewf")
kh6 = HocSinh(1,"along",10,"wefw")
kh7 = HocSinh(1,"along",2.5,"wefw")
kh8 = HocSinh(1,"along",1.5,"wefw")
kh1 = HocSinh(1,"Along",2,"fwef")
kh2 = HocSinh(1,"huy",2,"wefw")
kh3 = HocSinh(1,"huy",7,"wefw")
kh4 = HocSinh(1,"huy",10,"wefw")
kh5 = HocSinh(1,"huy",6.6,"wefw")
kh300 = HocSinh(1,"huy",1,"wefw")

Linked_List.themSinhVien(kh300)
Linked_List.themSinhVien(kh3)
Linked_List.themSinhVien(kh4)
Linked_List.themSinhVien(kh5)
Linked_List.themSinhVien(kh6)
Linked_List.themSinhVien(kh1)
Linked_List.themSinhVien(kh2)
Linked_List.themSinhVien(kh7)
Linked_List.themSinhVien(kh8)
Linked_List.themSinhVien(kh9)

# Linked_List.in_DS()
# Linked_List.sap_xep_theo_diem()
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh1)
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh5)
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh6)
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh7)
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh8)
# Linked_List.chen_hoc_sinh_vao_ds_dasx(kh9)
# Linked_List.in_DS()

while True:
    os.system("cls")
    print("\n\n\t\t====================== MENU =======================", end='')
    print("\n\t1. Chèn một học sinh mới vào danh sách cuối cùng.",end='')
    print("\n\t2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm",end='')
    print("\n\t3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp",end='')
    print("\n\t4. Lấy danh sách sinh viên có Điểm lớn hơn x.",end='')
    print("\n\t5. Tìm kiếm k sinh viên có Điểm cao nhất",end='')
    print("\n\t6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x",end='')
    print("\n\t7. In danh sách.",end='')
    print("\n\t8. In danh sách sinh viên ra file.",end='')
    print("\n\n\t\t====================== MENU =======================\n",end='')
    n  = int(input("Nhập lựa chọn mà bạn muốn(nhập 0 để thoát): "))
    if n==1:
        ma_sv = int(input("Nhập mã sinh viên: "))
        ho_ten = input("Nhập họ và tên của học sinh: ")
        diem = float(input("Nhập điểm: "))
        mon_hoc = input("Nhập môn học: ")
        tmp = HocSinh(ma_sv,ho_ten,diem,mon_hoc)
        Linked_List.themSinhVien(tmp)
    elif n==2:
        Linked_List.sap_xep_theo_diem()
        print("Đã sắp xếp thành công !!")
        input("Nhấn enter để tiếp tục !!!")
    elif n==3:
        ma_sv = int(input("Nhập mã sinh viên: "))
        ho_ten = input("Nhập họ và tên của học sinh: ")
        diem = float(input("Nhập điểm: "))
        mon_hoc = input("Nhập môn học: ")
        tmp = HocSinh(ma_sv,ho_ten,diem,mon_hoc)
        Linked_List.chen_hoc_sinh_vao_ds_dasx(tmp)
        input("Nhấn enter để tiếp tục !!!")
    elif n==4:
        diem1 = int(input("Nhập điểm bạn mong muốn: "))
        Linked_List.lay_ds_sv_diem_lon_hon_x(diem1)
        input("Nhấn enter để tiếp tục !!!")
    elif n==5:
        Linked_List.tim_kiem_sinh_vien_diem_cao_nhat()
        input("Nhấn enter để tiếp tục")
    elif n==6:
        diem1 = int(input("Nhập điểm bạn mong muốn: "))
        Linked_List.loai_bo_sinh_vien_diem_nho_hon_x(diem1)
    elif n==7:
        Linked_List.in_DS()
        input("Nhấn enter để tiếp tục")
    elif n==8:
        Linked_List.inThongTinRaFile()
    elif n==0:
        print("Kết thúc chương trình !!!")
        break
    else:
        print("nhập sai yêu cầu nhập lại !!!")
        input("Nhấn enter để tiếp tục !!!")