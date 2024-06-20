#Viết chương trình tìm số lớn thứ hai trong một list
def timSoLonThuHai(list):
    so_lon_thu_hai = sorted(list)[-2]
    return so_lon_thu_hai

danh_sach_so = [10,20,30,50,100]
print(danh_sach_so)
ket_qua = timSoLonThuHai(danh_sach_so)
print(f"Số lớn thứ hai trong danh sách là {ket_qua}")