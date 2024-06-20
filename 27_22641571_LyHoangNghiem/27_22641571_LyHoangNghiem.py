import os
class QuanLyNuocTieuThu:
    def __init__(self,MaDH, TenDH, ThangNam,SoNuocTieuThu):
        self.MaDH = MaDH
        self.TenDH = TenDH
        self.ThangNam = ThangNam
        self.SoNuocTieuThu = SoNuocTieuThu
    def __str__(self):
        return f"MaDH: {self.MaDH}, TenDH: {self.TenDH}, ThangNam: {self.ThangNam}, SoNuocTieuThu: {self.SoNuocTieuThu}"


class Node:
    def __init__(self, data):
        self.data = data
        self.pLeft = None
        self.pRight = None
class CayNhiPhanTimKiem:
    def __init__(self):
        self.root = None
    def themVaoCay(self,data):
        def themVaoCay1(root,data):
            if root == None:
                return Node(data)
            elif root.data.MaDH > data.MaDH:
                root.pLeft = themVaoCay1(root.pLeft, data)
            elif root.data.MaDH < data.MaDH:
                root.pRight = themVaoCay1(root.pRight, data)
            else:
                print("Trùng mã đơn hàng!!!")
                return root
            return root
        self.root = themVaoCay1(self.root, data)

    def LNR(self):
        def LNR1(root):
            if root is not None:
                LNR1(root.pLeft)
                print(root.data.SoNuocTieuThu)
                LNR1(root.pRight)
        LNR1(self.root)
    #Duyệt cây theo thứ tự LRN nếu Node nào có giá trị SoNuocTieuThu thoa dieu kien chia hết cho 2 thì đưa vào hàng đợi.
    #Xuất dữ liệu hàng đợi ra màn hình
    def LRN(self):
        def LRN1(root):
            if root is not None:
                LRN1(root.pLeft)
                LRN1(root.pRight)
                if root.data.SoNuocTieuThu % 2 == 0:
                    print(root.data.SoNuocTieuThu)
        LRN1(self.root)
    #Cho biết tổng doanh thu của tất cả đồng hồ. Biết rằng đơn giá được tính như: nếu số KW dưới 5 thì đơn giá là 1000, từ 5 đến 10 là 2000
    #còn lại là 3000. Thành tiền mỗi đồng hồ bằng SoNuocTieuThu * DonGia 
    def tongDoanhThu(self):
        def tongDoanhThu1(root):
            if root == None:
                return 0
            else:
                if root.data.SoNuocTieuThu < 5:
                    DonGia = 1000
                elif 5 <= root.data.SoNuocTieuThu <= 10:
                    DonGia = 2000
                else:
                    DonGia = 3000
                return root.data.SoNuocTieuThu * DonGia + tongDoanhThu1(root.pLeft) + tongDoanhThu1(root.pRight)
        return tongDoanhThu1(self.root)
    #Tìm kiếm một Node có MaDH được nhập từ bàn phím. Nếu thấy xuất giá trị Node này ra màn hình. Không thấy thì thông báo không tìm thấy
    def timKiem(self,MaDH):
        def timKiem1(root, MaDH):
            if root is None:
                return None
            elif root.data.MaDH == MaDH:
                return root.data
            elif root.data.MaDH > MaDH:
                return timKiem1(root.pLeft, MaDH)
            else:
                return timKiem1(root.pRight, MaDH)
        result = timKiem1(self.root, MaDH)
        if result is not None:
            print(result.__str__())
        else:
            print("Không tìm thấy!!!")
    #Nhập vào MaDH cần sửa thông tin. Hỏi người dùng có muốn sửa lại số nước tiêu thụ không,
    #nếu muốn thì cho phép người dùng cập nhập lại số nước tiêu thụ
    def suaThongTin(self,MaDH):
        def suaThongTin1(root, MaDH):
            if root is None:
                return None
            elif root.data.MaDH == MaDH:
                print("Nhập số nước tiêu thụ mới:")
                root.data.SoNuocTieuThu = int(input())
                return root.data
            elif root.data.MaDH > MaDH:
                return suaThongTin1(root.pLeft, MaDH)
            else:
                return suaThongTin1(root.pRight, MaDH)
        result = suaThongTin1(self.root, MaDH)
        if result is not None:
            print(result.__str__())
        else:
            print("Không tìm thấy mã hóa đơn để sửa!!!")
    #Xóa một Node có SoNuocTieuThu được nhập từ bàn phím. Xuất giá trị các Node sau khi xóa Node này. Vẽ lại cây sau khi xóa Node này
    def xoaNodeBatKy(self,x):
        if self.root is None:
            return
        if self.root != None and self.root.pLeft == None and self.pRight == None:
            self.root = None
        
        t=self.root
        parent = t
        while t != None and t.data.SoNuocTieuThu != x:
            parent = t
            if t.data.SoNuocTieuThu > x:
                t = t.pLeft
            elif t.data.SoNuocTieuThu < x:
                t = t.pRight
        if t != None:
            q = None

            if t.pLeft != None and t.pRight != None:
                parent = t
                r = t.pLeft 
                while r.pRight != None:
                    parent = r
                    r = r.pRight
                t.data = r.data
                t = r
            if t.pLeft == None:
                q = t.pRight
            else:
                q = t.pLeft
            if parent.data.SoNuocTieuThu >= t.data.SoNuocTieuThu:
                if t.data.SoNuocTieuThu == self.root.data.SoNuocTieuThu:
                    if self.root.pLeft == None and self.root.pRight != None:
                        self.root = self.root.pRight
                    elif self.root.pLeft != None and self.root.pRight == None:
                        self.root = self.root.pLeft
                else:
                    parent.pLeft = q
            else:
                parent.pRight = q
            del t


bnt = CayNhiPhanTimKiem()
tmp = QuanLyNuocTieuThu(71,"DH1","01/2021",22)
bnt.themVaoCay(tmp)
tmp = QuanLyNuocTieuThu(15,"DH2","10/2022",64)
bnt.themVaoCay(tmp)
tmp = QuanLyNuocTieuThu(64,"DH3","02/2023",15)
bnt.themVaoCay(tmp)
tmp = QuanLyNuocTieuThu(22,"DH4","06/2024",71)
bnt.themVaoCay(tmp)

while (True):
    os.system("cls")
    print("1. Thêm vào cây ")
    print("2. Thêm vào cây 1 Node có SoNuocTieuThu là số 27")
    print("3. Duyệt cây theo thứ tự LNR (Chỉ ghi kết quả trường SoNuocTieuThu)")
    print("4. Duyệt cây theo thứ tự LRN của trường SoNuocTieuThu (thỏa điều kiện chia hết cho 2)")
    print("5. Tính tổng doanh thu")
    print("6. Tìm kiếm một Node có MaDH được nhập từ bàn phím")
    print("7. Nhập vào MaDH cần sửa thông tin")
    print("8. Xóa một Node có SoNuocTieuThu được nhập từ bàn phím")
    print("9. Thoát")
    choice = input("Chọn chức năng: ")
    if choice == "1":
        MaDH = int(input("Nhập MaDH: "))
        TenDH = input("Nhập TenDH: ")
        ThangNam = input("Nhập ThangNam: ")
        SoNuocTieuThu = int(input("Nhập SoNuocTieuThu: "))
        tmp = QuanLyNuocTieuThu(MaDH, TenDH, ThangNam, SoNuocTieuThu)
        bnt.themVaoCay(tmp)
        os.system("pause")
    elif choice == "2":
        tmp = QuanLyNuocTieuThu(27,"DH5","07/2025",27)
        bnt.themVaoCay(tmp)
        bnt.LNR()

        os.system("pause")
    elif choice == "3":
        bnt.LNR()
        os.system("pause")
    elif choice == "4":
        bnt.LRN()
        os.system("pause")
    elif choice == "5":
        print("Tổng doanh thu: ",bnt.tongDoanhThu())
        os.system("pause")
    elif choice == "6":
        MaDH = int(input("Nhập MaDH cần tìm: "))
        bnt.timKiem(MaDH)
        os.system("pause")
    elif choice == "7":
        MaDH = int(input("Nhập MaDH cần sửa: "))
        #người dùng chọn (y/n)
        if input("Bạn có muốn sửa lại số nước tiêu thụ không (y/n): ") == "y":
            bnt.suaThongTin(MaDH)
        else:
            print("Không sửa!!!")
        
        os.system("pause")
    elif choice == "8":
        x = int(input("Nhập số nước tiêu thụ cần xóa: "))
        bnt.xoaNodeBatKy(x)
        os.system("pause")
    elif choice == "9":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        os.system("pause")

   