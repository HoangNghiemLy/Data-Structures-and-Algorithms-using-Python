#Viết chương trình tìm số lần xuất hiện của mỗi ký tự trong một chuỗi
def timSoLanXuatHienCuaKyTu(chuoi):
    kyTu = []
    soLanXuatHien = []
    for i in chuoi:
        if i not in kyTu:
            kyTu.append(i)
            soLanXuatHien.append(chuoi.count(i))
    return kyTu, soLanXuatHien
chuoi = input("Nhập chuỗi: ")
kyTu, soLanXuatHien = timSoLanXuatHienCuaKyTu(chuoi)
for i in range(len(kyTu)):
    print(f"Số lần xuất hiện của ký tự {kyTu[i]} là {soLanXuatHien[i]}")
    