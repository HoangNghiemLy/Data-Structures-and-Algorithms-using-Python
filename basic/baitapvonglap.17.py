#Viết chương trình tìm ký tự xuất hiện nhiều lần nhất trong một chuỗi

def timKyTuXuatHienNhieuNhat(chuoi):
    kyTu = ""
    soLanXuatHien = 0
    for i in chuoi:
        if chuoi.count(i) > soLanXuatHien:
            soLanXuatHien = chuoi.count(i)
            kyTu = i
    return kyTu
chuoi = input("Nhập chuỗi: ")
print(f"Ký tự xuất hiện nhiều nhất trong chuỗi là: {timKyTuXuatHienNhieuNhat(chuoi)}")