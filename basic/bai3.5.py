#Viết chương trình tìm số nhỏ nhất trong một list
def timSoNhoNhat(list):
    so_nho_nhat = min(list)
    return so_nho_nhat

danh_sach_so = [10,20,-1,-2,5,100,200]
print(danh_sach_so)
ket_qua = timSoNhoNhat(danh_sach_so)
print(f"Số nhỏ nhất trong danh sách là {ket_qua}")
