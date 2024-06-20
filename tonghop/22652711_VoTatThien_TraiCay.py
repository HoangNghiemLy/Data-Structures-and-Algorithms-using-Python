import os
import matplotlib.pyplot as plt
class TraiCay:
    def __init__(self, tenTraiCay, maLoaiTraiCay, soLuong, giaBan):
        self.__tenTraiCay = tenTraiCay
        self.__maLoaiTraiCay = maLoaiTraiCay
        self.__soLuong = soLuong
        self.__giaBan = giaBan

    def getTenTraiCay(self):
        return self.__tenTraiCay

    def setTenTraiCay(self, tenTraiCay):
        self.__tenTraiCay = tenTraiCay

    def getMaLoaiTraiCay(self):
        return self.__maLoaiTraiCay

    def setMaLoaiTraiCay(self, maLoaiTraiCay):
        self.__maLoaiTraiCay = maLoaiTraiCay

    def getSoLuong(self):
        return self.__soLuong

    def setSoLuong(self, soLuong):
        self.__soLuong = soLuong

    def getGiaBan(self):
        return self.__giaBan

    def setGiaBan(self, giaBan):
        self.__giaBan = giaBan

    def inThongTin(self):
        return "Mã: " + self.__maLoaiTraiCay + " Tên trái cây: " + self.__tenTraiCay + " Gía bán: " + str(self.__giaBan) + " Số lượng " + str(self.__soLuong)
class NODE:
    def __init__(self, data):
        self.data = data
        self.pNext = None
pHead = None
class Linked_List:

    def timKiemTraiCay(self, id):
        tmp = pHead
        while tmp != None:
            if tmp.data.getMaLoaiTraiCay() == id:
                return tmp.data
            tmp = tmp.pNext
        return None

    def them(self,data):
        global pHead
        tmp = NODE(data)
        if self.timKiemTraiCay(data.getMaLoaiTraiCay())!=None:
            print("Mã Đã tồn tại")
            return
        if pHead == None:
            pHead = tmp
        else:
            tmp.pNext = pHead
            pHead = tmp
    
    def inThongTin1(self):
        tmp = pHead
        while tmp != None:
            print(tmp.data.inThongTin())
            tmp = tmp.pNext
        return None

    def sapXepTangDan(self):
        global pHead
        tmp = pHead
        while tmp != None:
            tmp1 = tmp.pNext
            while tmp1 != None:
                if tmp.data.getSoLuong() > tmp1.data.getSoLuong():
                    tmp.data, tmp1.data = tmp1.data, tmp.data
                tmp1 = tmp1.pNext
            tmp = tmp.pNext

    def trungBinhGiaBan(self):
        tmp = pHead
        dem = 0
        sum = 0
        while tmp != None:
            sum += tmp.data.getGiaBan()
            dem += 1
            tmp = tmp.pNext
        rs = sum // dem
        return rs


l = Linked_List()

# l.them(TraiCay("Táo Mỹ", "1", 23, 20000))
# l.them(TraiCay("Táo Mỹ", "2", 53, 10000))
# l.them(TraiCay("Táo Mỹ", "3", 83, 60000))
# l.them(TraiCay("Táo Mỹ", "4", 13, 30000))
# l.them(TraiCay("Táo Mỹ", "5", 43, 50000))
# l.them(TraiCay("Táo Mỹ", "6", 13, 20000))
# l.them(TraiCay("Táo Mỹ", "7", 63, 10000))


while True:
    os.system("cls")
    print("1. Thêm loại trái cây.")
    print("2. In thông tin trái cây theo mã.")
    print("3. In toàn bộ trái cây có trong cửa hàng.")
    print("4. Sắp xếp trái cây theo giá tăng dần.")
    print("5. Gía trung bình từng loại trái cây.")
    n = int(input("Nhập lựa chọn bạn muốn(Nhập 0 để thoát): "))
    if n==1:
        maTraiCay = input("Nhập mã trái cây: ")
        ten = input("Tên trái cây: ")
        soLuong = int(input("Nhập số lượng: "))
        giaBan = float(input("Nhập giá bạn: "))
        tmp = TraiCay(ten, maTraiCay, soLuong, giaBan)
        l.them(tmp)
        input("Nhấn enter để tiếp tục !!!")
    elif n==2:
        maTraiCay = input("Nhập mã trái cây: ")
        i = l.timKiemTraiCay(maTraiCay)
        if i != None:
            print(i.inThongTin())
        else:
            print("Không tìm thấy !!!!")
        input("Nhấn enter để tiếp tục !!!")
    elif n==3:
        l.inThongTin1()
        input("Nhấn enter để tiếp tục !!!")
    elif n==4:
        l.sapXepTangDan()
        print("đã sắp xếp !!!")
        input("Nhấn enter để tiếp tục !!!")
    elif n==5:
        print(f"trung bình giá bán: {l.trungBinhGiaBan()} ")
        input("Nhấn enter để tiếp tục !!!")
    elif n==0:
        print("Thoát chương trình !!")
        break


