'''
Xây dựng list để lưu trữ danh sách sinh viên (Masv, TenSV, MonHoc, Diem). Ghi
nhiệm vụ sau:
1. Chèn một học sinh mới vào danh sách cuối cùng.
2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm
3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp
4. Lấy danh sách sinh viên có Điểm lớn hơn x.
5. Tìm kiếm k sinh viên có Điểm cao nhất
6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x.
7. Hợp nhất vào danh sách sinh viên.
8. In ra màn hình danh sách sinh viên.
9. Ghi danh sách học sinh ra file txt.
'''
class SinhVien:
    def __init__(self,masv,hoten,monhoc,diem):
        self.masv = masv
        self.hoten = hoten
        self.monhoc = monhoc
        self.diem = diem 
    def get_masv(self):
        return self.masv
    def set_masv(self,masv):
        self.masv = masv
    def get_hoten(self):
        return self.hoten
    def set_hoten(self,hoten):
        self.hoten = hoten
    def get_monhoc(self):
        return self.monhoc
    def set_monhoc(self,monhoc):
        self.monhoc = monhoc
    def get_diem(self):
        return self.diem
    def set_diem(self,diem):
        self.diem = diem
    def to_string(self):
        return f"Mã sinh viên: {self.masv}, Họ tên: {self.hoten}, Môn học: {self.monhoc}, Điểm: {self.diem}"
class NODE:
    def __init__(self,data):
        self.data = data
        self.nutketiep = None
class Linked_List:
    def __init__(self):
        self.pHead = None
    #1. Chèn một học sinh mới vào danh sách cuối cùng.
    def chen_sv_moi(self,sv):
        k = NODE(sv)
        if self.pHead == None:
            self.pHead = k
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.nutketiep == None:
                    tmp.nutketiep = k
                    break
                tmp = tmp.nutketiep
    #2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm
    def sap_xep_theo_diem(self):
        tmp = self.pHead
        while tmp != None:
            tmp1 = tmp.nutketiep
            while tmp1 != None:
                if tmp1.data.get_diem()<tmp.data.get_diem():
                    tmp1.data,tmp.data = tmp.data,tmp1.data
                tmp1 = tmp1.nutketiep
            tmp = tmp.nutketiep
    #3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp
    def chen_sv_moi_sap_xep(self,sv):
        k = NODE(sv)
        if self.pHead == None:
            self.pHead = k
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.nutketiep == None:
                    tmp.nutketiep = k
                    break
                tmp = tmp.nutketiep
            self.sap_xep_theo_diem()
    #4. Lấy danh sách sinh viên có Điểm lớn hơn x.
    def lay_sv_diem_lon_hon_x(self,x):
        tmp = self.pHead
        while tmp != None:
            if tmp.data.get_diem() > x:
                print(tmp.data.to_string())
            tmp = tmp.nutketiep
    #5. Tìm kiếm k sinh viên có Điểm cao nhất
    def tim_k_sv_cao_nhat(self,k):
        #viết phương thức sắp xếp điểm giảm dần
        if not self.pHead or k <= 0:
            return None
        top_students = []
        tmp = self.pHead
        while tmp != None and k > 0:
            top_students.append(tmp.data)
            tmp = tmp.nutketiep
            k -= 1
        top_students.sort(key = lambda student: student.get_diem(),reverse = True)
        return top_students
    
        
    


    #6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x.
    def loai_bo_sv_diem_nho_hon_x(self,x):
        tmp = self.pHead
        while tmp != None:
            if tmp.data.get_diem() < x:
                self.pHead = tmp.nutketiep
            tmp = tmp.nutketiep


    #7. Hợp nhất vào danh sách sinh viên.
    def hop_nhat_sv(self,sv):
        k = NODE(sv)
        if self.pHead == None:
            self.pHead = k
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.nutketiep == None:
                    tmp.nutketiep = k
                    break
                tmp = tmp.nutketiep
    #8. In ra màn hình danh sách sinh viên.
    def in_ds_sv(self):
        tmp = self.pHead
        while tmp != None:
            print(tmp.data.to_string())
            tmp = tmp.nutketiep
    #9. Ghi danh sách học sinh ra file txt.
    def ghi_ds_sv_ra_file(self):
        fr = open("dssv.txt",mode = 'w', encoding = 'utf-8',)
        tmp = self.pHead
        while tmp != None:
            fr.write(str(tmp.data.to_string()) + "\n")
            tmp = tmp.nutketiep
def main():
    ds = Linked_List()
    while True:
        print("===Menu===")
        print("1. Chèn một học sinh mới vào danh sách cuối cùng.")
        print("2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm")
        print("3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp")
        print("4. Lấy danh sách sinh viên có Điểm lớn hơn x.")
        print("5. Tìm kiếm k sinh viên có Điểm cao nhất")
        print("6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x.")
        print("7. Hợp nhất vào danh sách sinh viên.")
        print("8. In ra màn hình danh sách sinh viên.")
        print("9. Ghi danh sách học sinh ra file txt.")
        chon = int(input("Mời bạn chọn: "))
        if chon == 1:
            masv = input("Nhập mã sinh viên: ")
            hoten = input("Nhập họ tên: ")
            monhoc = input("Nhập môn học: ")
            diem = float(input("Nhập điểm: "))
            sv = SinhVien(masv,hoten,monhoc,diem)
            ds.chen_sv_moi(sv)
        elif chon == 2:
            ds.sap_xep_theo_diem()
            print("Danh sách sau khi sắp xếp: ")
            ds.in_ds_sv()
        elif chon == 3:
            masv = input("Nhập mã sinh viên: ")
            hoten = input("Nhập họ tên: ")
            monhoc = input("Nhập môn học: ")
            diem = float(input("Nhập điểm: "))
            sv = SinhVien(masv,hoten,monhoc,diem)
            ds.chen_sv_moi_sap_xep(sv)
        elif chon == 4:
            x = float(input("Nhập x: "))
            ds.lay_sv_diem_lon_hon_x(x)
        elif chon == 5:
            k = int(input("Nhập k: "))
            top_k_students = ds.tim_k_sv_cao_nhat(k)
            if top_k_students:
                print(f'{k} sinh viên có điểm cao nhất là: ')
                for student in top_k_students:
                    print(student.to_string())
            else:
                print("Danh sách sinh viên rỗng hoặc giá trị k ko hợp lệ!!!")
        elif chon == 6:
            x = float(input("Nhập x: "))
            ds.loai_bo_sv_diem_nho_hon_x(x)
        elif chon == 7:
            masv = input("Nhập mã sinh viên: ")
            hoten = input("Nhập họ tên: ")
            monhoc = input("Nhập môn học: ")
            diem = float(input("Nhập điểm: "))
            sv = SinhVien(masv,hoten,monhoc,diem)
            ds.hop_nhat_sv(sv)
        elif chon == 8:
            ds.in_ds_sv()
        elif chon == 9:
            ds.ghi_ds_sv_ra_file()
        else:
            break
if __name__ == "__main__":
    main()


    