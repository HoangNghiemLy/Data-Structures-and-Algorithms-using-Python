#Viết chương trình tìm số lớn nhất trong một list không sử dụng hàm max()
def timSoLonNhat(list):
    so_lon_nhat = list[0]
    for i in list:
        if i > so_lon_nhat:
            so_lon_nhat = i
    return so_lon_nhat

danh_sach_so = [5,10,15,20,2]
print(danh_sach_so)
ket_qua = timSoLonNhat(danh_sach_so)
print(f"Số lớn nhất trong danh sách là {ket_qua}")