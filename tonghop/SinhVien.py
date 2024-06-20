'''
2.Để lưu trữ các thông tin về sinh viên trong một trường Đại Học người ta dùng cấu trúc  sau
struct SINHVIEN{	int MASV;
			char HOTEN[40];
			char DIACHI[50];
			float DIEM;};
Viết chương trình yêu cầu thực hiện các công việc sau:
1.Nhập n sinh viên
2.Xuất danh sách sinh viên vừa nhập
3.Xuất danh sách theo thứ tự tăng dần của Masv bằng các thuật toán Sắp xếp đã được học.
4.Xuất danh sách theo thứ tự tăng dần của Hoten bằng các thuật toán Sắp xếp đã được học.
5.Viết thủ tục tìm kiếm sinh viên có mã số X (X được nhập từ bàn phím)
'''

class SinhVien:

    def __init__(self, masv, hoten, diachi, diem):
        self.masv = masv
        self.hoten = hoten
        self.diachi = diachi
        self.diem = diem

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.masv, self.hoten, self.diachi, self.diem)
    
    
    def nhap(self):
        self.masv = int(input("Nhập mã sinh viên: "))
        self.hoten = input("Nhập họ tên sinh viên: ")
        self.diachi = input("Nhập địa chỉ sinh viên: ")
        self.diem = float(input("Nhập điểm sinh viên: "))

    def xuat(self):
        print("{0:10} {1:30} {2:50} {3:3}".format(self.masv, self.hoten, self.diachi, self.diem))

    #.Xuất danh sách theo thứ tự tăng dần của Masv bằng các thuật toán Sắp xếp đã được học.
    def sapxep_masv(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n, 1):
                if arr[i].masv > arr[j].masv:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    #4.Xuất danh sách theo thứ tự tăng dần của Hoten bằng các thuật toán Sắp xếp đã được học.
    def sapxep_hoten(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n, 1):
                if arr[i].hoten > arr[j].hoten:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    #5.Viết thủ tục tìm kiếm sinh viên có mã số X (X được nhập từ bàn phím)
    def timkiem_masv(self, arr, x):
        n = len(arr)
        for i in range(n):
            if arr[i].masv == x:
                return arr[i]
        return None
    
    def menu(self):
        print("1.Nhập n sinh viên")
        print("2.Xuất danh sách sinh viên vừa nhập")
        print("3.Xuất danh sách theo thứ tự tăng dần của Masv bằng các thuật toán Sắp xếp đã được học.")
        print("4.Xuất danh sách theo thứ tự tăng dần của Hoten bằng các thuật toán Sắp xếp đã được học.")
        print("5.Viết thủ tục tìm kiếm sinh viên có mã số X (X được nhập từ bàn phím)")
        print("6.Thoát chương trình")
        print()
        chon = int(input("Nhập tùy chọn: "))
        return chon
    
    def main(self):

        arr = []
        while True:
            chon = self.menu()
            if chon == 1:
                n = int(input("Nhập số lượng sinh viên: "))
                for i in range(n):
                    sv = SinhVien(0, '', '', 0)
                    sv.nhap()
                    arr.append(sv)
            elif chon == 2:
                print("{0:10} {1:30} {2:50} {3:3}".format("Mã SV", "Họ tên", "Địa chỉ", "Điểm"))
                for i in range(len(arr)):
                    arr[i].xuat()
            elif chon == 3:
                arr = self.sapxep_masv(arr)
                print("{0:10} {1:20} {2:20} {3:10}".format("Mã SV", "Họ tên", "Địa chỉ", "Điểm"))
                for i in range(len(arr)):
                    arr[i].xuat()
            elif chon == 4:
                arr = self.sapxep_hoten(arr)
                print("{0:10} {1:20} {2:20} {3:10}".format("Mã SV", "Họ tên", "Địa chỉ", "Điểm"))
                for i in range(len(arr)):
                    arr[i].xuat()
            elif chon == 5:
                x = int(input("Nhập mã sinh viên cần tìm: "))
                sv = self.timkiem_masv(arr, x)
                if sv == None:
                    print("Không tìm thấy sinh viên có mã số {0}".format(x))
                else:
                    print("{0:10} {1:20} {2:20} {3:10}".format("Mã SV", "Họ tên", "Địa chỉ", "Điểm"))
                    sv.xuat()
            elif chon == 6:
                break
            else:
                print("Nhập sai, hãy nhập lại...")
            print()

    
if __name__ == "__main__":
    sv = SinhVien(0, '', '', 0)
    sv.main()






    