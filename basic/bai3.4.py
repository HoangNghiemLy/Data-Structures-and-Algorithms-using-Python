#Viết chương trình tìm số lớn nhất trong một list
def timSoLonNhat(list):
    so_lon_nhat = max(list)
    return so_lon_nhat

danh_sach_so = [10,20,50,100,200,-2,-3]
print(danh_sach_so)
ket_qua = timSoLonNhat(danh_sach_so)
print(f"Số lớn nhất trong danh sách là {ket_qua}")

