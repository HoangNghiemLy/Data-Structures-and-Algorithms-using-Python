'''
2) Tạo menu và thực hiện các chức năng sau trên DSLK đơn chứa số nguyên:
0. Thêm phần tử vào danh sách
1. Thêm một số pt vào cuối ds
2. Thêm 1 pt vào trước pt nào đó
3. In ds
4. In ds theo thứ tự ngược
5. Tìm GTNN, GTLN trong ds
6. Tính tổng số âm, tổng số dương trong ds
7. Tính tích các số trong ds
8. Tính tổng bình phương của các số trong ds
9. Nhập x, xuất các số là số nguyên tố của x
10.Nhập x, xuất các số là ước số của x
11.Nhập x, tìm giá trị đầu tiên trong ds mà >x.
12.Xuất số nguyên tố cuối cùng trong ds
13.Đếm các số nguyên tố
14.Kiểm tra xem ds có phải đã được sắp tăng không
15.Kiểm tra xem ds có các pt đối xứng nhau hay không
16.Xóa pt cuối
17.Xóa pt đầu
18.Hủy toàn bộ ds
'''
import os

class Nut2:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None
class DSLK2:

    def __init__(self):
        self.dau = None
        self.cuoi = None
    def them_cuoi(self,gia_tri):
       
        nut = Nut2(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.nut_ke_tiep = nut
            self.cuoi = nut

    def them_truoc(self,gia_tri,pt):

        nut = Nut2(gia_tri)
        hien_tai = self.dau

        if self.dau == None: return

        elif self.dau.gia_tri == pt:
            nut.nut_ke_tiep = self.dau
            self.dau = nut

        while hien_tai.nut_ke_tiep != None:
            if hien_tai.nut_ke_tiep.gia_tri == pt:
                nut = Nut2(gia_tri)
                nut.nut_ke_tiep = hien_tai.nut_ke_tiep
                hien_tai.nut_ke_tiep = nut
                hien_tai = hien_tai.nut_ke_tiep
            hien_tai = hien_tai.nut_ke_tiep
        


    def in_ds(self):
        stt = 0
        hien_tai = self.dau
        kq = 'DS ['
        while hien_tai != None:
            stt += 1
            kq += str(hien_tai.gia_tri)
            if hien_tai.nut_ke_tiep != None: kq += ', '
            hien_tai = hien_tai.nut_ke_tiep
        kq += ']'
        print(kq)
        
       

    def in_ds_nguoc(self):
        truoc = None
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != None:
            sau = hien_tai.nut_ke_tiep
            hien_tai.nut_ke_tiep = truoc
            truoc = hien_tai
            hien_tai = sau
        self.dau = hien_tai
        hien_tai.nut_ke_tiep = truoc
        self.in_ds()

    def gtln(self):
        
        max = self.dau.gia_tri
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri > max:
                max = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return max
    def gtnn(self):
        min = self.dau.gia_tri
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri < min:
                min = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return min
    def tong_so_am(self):
        tong = 0
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri < 0:
                tong += hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return tong
    def tong_so_duong(self):
        tong = 0
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri > 0:
                tong += hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return tong
    def tich(self):
        tich = 1
        hien_tai = self.dau
        while hien_tai != None:
            tich *= hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return tich
    def tong_binh_phuong(self):
        tong  = 0
        hien_tai = self.dau
        while hien_tai != None:
            tong += hien_tai.gia_tri ** 2
            hien_tai = hien_tai.nut_ke_tiep
        return tong
    def so_nguyen_to(self,x):
        #nhập x và xuất các số là số nguyên tố của x
        hien_tai = self.dau
        kq = 'DS ['
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri % x == 0:
                kq += str(hien_tai.gia_tri)
                if hien_tai.nut_ke_tiep != None:
                    kq += ', '
            hien_tai = hien_tai.nut_ke_tiep
        kq += ']'
        print(kq)
    def uoc_so(self,x):
        #nhập x và xuất các số là ước số của x
        hien_tai = self.dau
        kq = 'DS ['
        while hien_tai.nut_ke_tiep != None:
            if x % hien_tai.gia_tri == 0:
                kq += str(hien_tai.gia_tri)
                if hien_tai.nut_ke_tiep != None:
                    kq += ', '
            hien_tai = hien_tai.nut_ke_tiep
        kq += ']'
        print(kq)
    def gt_dau_tien_lon_hon_x(self,x):
        #nhập x, tìm giá trị đầu tiên trong ds mà >x.
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri > x:
                return hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
    def so_nguyen_to_cuoi_cung(self):
        #Xuất số nguyên tố cuối cùng trong ds
        hien_tai = self.dau
        kq = 0
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri % 2 == 0:
                kq = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return kq
    def dem_so_nguyen_to(self):
        #Đếm các số nguyên tố trong ds
        hien_tai = self.dau
        kq = 0
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri % 2 == 0:
                kq += 1
            hien_tai = hien_tai.nut_ke_tiep
        return kq
    def kiem_tra_sap_xep_tang(self):
        #Kiểm tra xem ds có phải đã được sắp tăng không
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri > hien_tai.nut_ke_tiep.gia_tri:
                return False
            hien_tai = hien_tai.nut_ke_tiep
        return True
    def kiem_tra_doi_xung(self):
        

        #Kiểm tra xem ds có các pt đối xứng nhau hay không
        mang = []
        hien_tai = self.dau
        truoc = None 
        while hien_tai!= None:
            mang.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        n= len(mang)
        for i in range(len(mang)//2):
            if mang[i] != mang[n-1-i]:
                return False
        return True   
            



       
    
        
    
    
    def xoa_cuoi(self):
        #Xóa pt cuối
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.nut_ke_tiep == self.cuoi:
                hien_tai.nut_ke_tiep = None
                self.cuoi = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
    def xoa_dau(self):
        #Xóa pt đầu
        self.dau = self.dau.nut_ke_tiep
    def huy_toan_bo(self):
        #Hủy toàn bộ ds
        self.dau = None
        self.cuoi = None

    def them(self, gia_tri):
        nut = Nut2(gia_tri)
        if self.dau==None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.nut_ke_tiep=nut
            self.cuoi = nut


