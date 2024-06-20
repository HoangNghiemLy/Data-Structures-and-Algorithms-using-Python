#Viết chương trình tạo một chuỗi mới bằng cách đổi chữ hoa thành chữ thường và ngược lại
def doiChuHoaChuThuong(chuoi):
    return chuoi.swapcase()
chuoi = input("Nhập chuỗi cần đổi: ")
print(f"Chuỗi sau khi đổi là {doiChuHoaChuThuong(chuoi)}")
