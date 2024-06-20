#Viết chương trình tính số lần xuất hiện của một phần tử trong một list
def tinhSoLanXuatHien(list, phan_tu):
    return list.count(phan_tu)

danh_sach_so = [10,20,30,40,50,10,10,10,10]
print(danh_sach_so)
ket_qua = tinhSoLanXuatHien(danh_sach_so, 10)
print(f"Số lần xuất hiện của phần tử 10 trong danh sách là {ket_qua}")