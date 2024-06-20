#Viết chương trình nhập vào một chuỗi từ bàn phím và đưa ra màn hình chuỗi sau khi xóa bỏ các dấu cách (nếu có)
def xoaDauCach(chuoi):
    return chuoi.replace(" ","")
chuoi = input("Nhập chuỗi cần xóa dấu cách: ")
print(f"Chuỗi sau khi xóa dấu cách là: {xoaDauCach(chuoi)}")
