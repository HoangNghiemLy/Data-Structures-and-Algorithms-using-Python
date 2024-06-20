'''
Quản lý khách hàng xếp hàng mua vé tại nhà ga. Thông tin lưu trữ cho khách hàng gồm: 
số CMND (String), tên khách hàng, ga đến, giá tiền (double).  
sử dụng danh sách liên kết đơn để lưu trữ
Sử dụng stack và queue để thêm và bán vé
Tạo hệ thống menu gồm các mục:
Thêm một khách hàng mới vào hàng đợi mua vé.
In thông tin khách hàng theo số CMND.
In toàn bộ khách hàng đang chờ mua vé ai vào trước sẽ xuất trước.
Sắp xếp khách hàng theo giá vé tăng dần.
Hiển thị danh sách các ga đang chờ mua vé.
Số vé tương ứng cho ga đang chờ mua vé.


'''
import os
class KhachHangMuaVe:
    def __init__(self,cmnd,ten,gaden,giave):
        self.cmnd = cmnd
        self.ten = ten
        self.gaden = gaden
        self.giave = giave
    def getCMND(self):
        return self.cmnd
    def setCMND(self,cmnd):
        self.cmnd = cmnd
    def getTen(self):
        return self.ten
    def setTen(self,ten):
        self.ten = ten
    def getGaDen(self):
        return self.gaden
    def setGaDen(self,gaden):
        self.gaden = gaden
    def getGiaVe(self):
        return self.giave
    def setGiaVe(self,giave):
        self.giave = giave

    def hienthi(self):
        return self.cmnd + " - " + self.ten + " - " + self.gaden + " - " + str(self.giave)
class HeThongVeTau:
    def __init__(self,data):
        self.data = data
        self.pNext = None
pHead = None
class Linked_List:
    def them(self, data):
        global pHead
        tmp = HeThongVeTau(data)
        if pHead == None:
            pHead = tmp
        else:
            tmp.pNext = pHead
            pHead = tmp
    
    def inThongTin1(self):
        tmp = pHead
        while tmp != None:
            print(tmp.data.hienthi())
            tmp = tmp.pNext
            
        

    def sapXepTangDan(self):
        global pHead
        tmp = pHead
        while tmp != None:
            tmp1 = tmp.pNext
            while tmp1 != None:
                if tmp.data.getGiaVe() > tmp1.data.getGiaVe():
                    tmp.data, tmp1.data = tmp1.data, tmp.data
                tmp1 = tmp1.pNext
            tmp = tmp.pNext

    def trungBinhGiaBan(self):
        tmp = pHead
        dem = 0
        sum = 0
        while tmp != None:
            sum += tmp.data.getGiaVe()
            dem += 1
            tmp = tmp.pNext
        rs = sum // dem
        return rs
    
    def hienthidsgadangchomuave(self):
        ds=[]
        tmp = pHead
        while tmp != None:
            ds.append(tmp.data.getGaDen())
            tmp = tmp.pNext
        return set(ds)
    def hienthisove(self,gaden):
        dem=0
        tmp = pHead
        while tmp != None:
            if tmp.data.getGaDen()==gaden:
                dem+=1
            tmp = tmp.pNext
        return dem
    def timkiem(self,cmnd):
        tmp=pHead
        while tmp != None:
            if tmp.data.getCMND()==cmnd:
                return tmp.data
            tmp=tmp.pNext
        return None
    def xoa(self,cmnd):
        global pHead
        if pHead == None:
            return
        if pHead.data.getCMND() == cmnd:
            tmp = pHead
            pHead = pHead.pNext
            del tmp
            return
        tmp = pHead
        while tmp.pNext != None:
            if tmp.pNext.data.getCMND() == cmnd:
                tmp1 = tmp.pNext
                tmp.pNext = tmp1.pNext
                del tmp1
                return
            tmp = tmp.pNext

l = Linked_List()
while True:
    os.system("cls")
    print("1. Thêm một khách hàng mới vào đầu hàng đợi mua vé.")
    print("2. In thông tin khách hàng theo số CMND.")
    print("3. In toàn bộ khách hàng đang chờ mua vé.")
    print("4. Sắp xếp khách hàng theo giá vé tăng dần.")
    print("5. Hiển thị danh sách các ga đang chờ mua vé.")
    print("6. Số vé tương ứng cho ga đang chờ mua vé.")
    print("7. Tìm kiếm vé theo số CMND.")
    print("8. Trung bình giá vé.")
    print("9. Xóa vé theo số CMND.")
    print("10. Thoát chương trình.")
    chon = int(input("Mời bạn chọn: "))
    if chon == 1:
        cmnd = input("Nhập số CMND: ")
        ten = input("Nhập tên khách hàng: ")
        gaden = input("Nhập ga đến: ")
        giave = float(input("Nhập giá vé: "))
        l.them(KhachHangMuaVe(cmnd, ten, gaden , giave))
    elif chon == 2:
        cmnd = input("Nhập số CMND: ")
        tmp = pHead
        while tmp != None:
            if tmp.data.getCMND() == cmnd:
                print(tmp.data.hienthi())
                break
            tmp = tmp.pNext
        else:
            print("Không tìm thấy khách hàng này...")
    elif chon == 3:
        l.inThongTin1()
    elif chon == 4:
        l.sapXepTangDan()
        l.inThongTin1()
    elif chon == 5:
        print("Danh sách các ga đang chờ mua vé: ")
        for gaden in l.hienthidsgadangchomuave():
            print(gaden)
    elif chon == 6:
        gaden = input("Nhập ga đến: ")
        print("Số vé tương ứng cho ga đang chờ mua vé: ",l.hienthisove(gaden))
    elif chon == 7:
        cmnd = input("Nhập số CMND: ")
        tmp = l.timkiem(cmnd)
        if tmp != None:
            print(tmp.hienthi())
        else:
            print("Không tìm thấy khách hàng này...")
        
    elif chon == 8:
        print("Trung bình giá vé: ",l.trungBinhGiaBan())
    elif chon == 9:
        cmnd = input("Nhập số CMND: ")
        l.xoa(cmnd)

    elif chon == 10:
        break
    
    else:
        print("Nhập sai chức năng !!!")
    input("Nhấn enter để tiếp tục !!!")
print("Thoát chương trình !!")


