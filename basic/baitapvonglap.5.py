#Viết chương trình đếm số lượng ký tự trong một chuỗi dùng vòng lặp
def demSoLuongKyTu(chuoi):
    dem = 0
    for i in chuoi:
        dem += 1
    return dem

chuoi = input("Nhập chuỗi cần đếm: ")
print(f"Số lượng ký tự trong chuỗi là {demSoLuongKyTu(chuoi)}")
