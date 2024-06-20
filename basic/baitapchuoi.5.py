#Nhập vào một chuỗi và 1 kí tự bất kì từ bàn phím. Đếm số lần xuất hiện của kí tự đó trong chuỗi
def demSoLanXuatHienKiTu(chuoi,kitu):
    return chuoi.count(kitu)
chuoi = input("Nhập chuỗi cần đếm: ")
kitu = input("Nhập kí tự cần đếm: ")
print(f"Số lần xuất hiện của kí tự {kitu} trong chuỗi là: {demSoLanXuatHienKiTu(chuoi,kitu)}")

