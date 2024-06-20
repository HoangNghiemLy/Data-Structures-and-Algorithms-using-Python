'''
BÀI TẬP DANH SÁCH LIÊN KẾT ĐƠN
1) Viết chương trình nhập từ bàn phím các số nguyên cho đến khi nhập vào chuỗi rỗng. 
Các số nguyên này được đưa vào 1 danh sách. Xuất ra:
1. Số lượng các phần tử trong danh sách
2. Tổng giá trị của các số trong danh sách
3. Giá trị lớn nhất trong danh sách
4. Giá trị nhỏ nhất trong danh sách
5. Sắp xếp Danh sách theo thứ tự tăng dần
6. Sắp xếp Danh sách theo thứ tự giảm dần
7. Danh sách các phần tử có giá trị là chẵn
8. Tìm 1 phần tử có giá trị X trong danh sách
'''
class Nut:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.Nutketiep = None
class DSLK:
    def __init__(self):
        self.Dau = None
        self.Cuoi = None
    def them(self, gia_tri):
        nut = Nut(gia_tri)
        if self.Dau==None:
            self.Dau = nut
            self.Cuoi = nut
        else:
            self.Cuoi.Nutketiep=nut
            self.Cuoi = nut
    def in_ds(self):
        stt = 0
        hien_tai = self.Dau
        kq = 'DS ['
        while hien_tai != None: 
            stt += 1
            kq += str(hien_tai.gia_tri)
            if hien_tai.Nutketiep != None: kq += ', '
            hien_tai = hien_tai.Nutketiep
        kq += ']'
        print(kq)
    
    def soluongcacphantu(self):
        stt = 0
        hien_tai = self.Dau
        while hien_tai != None:
            stt += 1
            hien_tai = hien_tai.Nutketiep
        return stt
    def tonggiatri(self):
        tong = 0
        hien_tai = self.Dau
        while hien_tai != None:
            tong += hien_tai.gia_tri
            hien_tai = hien_tai.Nutketiep
        return tong
    def giatri_max(self):
        max = self.Dau.gia_tri
        hien_tai = self.Dau
        while hien_tai != None:
            if hien_tai.gia_tri > max:
                max = hien_tai.gia_tri
            hien_tai = hien_tai.Nutketiep
        return max
    def giatri_min(self):
        min = self.Dau.gia_tri
        hien_tai = self.Dau
        while hien_tai != None:
            if hien_tai.gia_tri < min:
                min = hien_tai.gia_tri
            hien_tai = hien_tai.Nutketiep
        return min
    def sapxep_tang(self):
        hien_tai = self.Dau
        while hien_tai != None:
            hien_tai2 = hien_tai.Nutketiep
            while hien_tai2 != None:
                if hien_tai.gia_tri > hien_tai2.gia_tri:
                    hien_tai.gia_tri, hien_tai2.gia_tri = hien_tai2.gia_tri, hien_tai.gia_tri
                hien_tai2 = hien_tai2.Nutketiep

            hien_tai = hien_tai.Nutketiep


    def sapxep_giam(self):
        hien_tai = self.Dau
        while hien_tai != None:
            hien_tai2 = hien_tai.Nutketiep
            while hien_tai2 != None:
                if hien_tai.gia_tri < hien_tai2.gia_tri:
                    hien_tai.gia_tri, hien_tai2.gia_tri = hien_tai2.gia_tri, hien_tai.gia_tri
                hien_tai2 = hien_tai2.Nutketiep
            hien_tai = hien_tai.Nutketiep
    def ds_chan(self):
        hien_tai = self.Dau
        kq = 'DS ['
        while hien_tai != None:
            if hien_tai.gia_tri%2==0:
                kq += str(hien_tai.gia_tri)
                if hien_tai.Nutketiep != None: kq += ',' 
            hien_tai = hien_tai.Nutketiep
        kq += ']'
        print(kq)
    #in danh sách theo thứ tự ngược lại dùng for
    
    def in_ds_nguoc(self):
        truoc = None
        hien_tai = self.Dau
        while hien_tai != None:
            sau = hien_tai.Nutketiep
            hien_tai.Nutketiep = truoc
            truoc = hien_tai
            hien_tai = sau
        self.Dau = truoc
        self.in_ds()
    
    #kiểm tra xem ds có các phần tử đối xứng nhau hay khong
    def doi_xung(self):
        hien_tai = self.Dau
        truoc = None
        while hien_tai != None:
            if hien_tai.gia_tri != truoc.gia_tri:
                return False
            truoc = hien_tai
            hien_tai = hien_tai.Nutketiep
        return True
    




    

            
