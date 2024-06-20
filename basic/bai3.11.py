#Viết chương trình tìm giá trị trung bình của các phần tử trong một list
def timGiaTriTrungBinh(list):
    gia_tri_trung_binh = sum(list)/len(list)
    return gia_tri_trung_binh

danh_sach_so = [10,20,30,40,50]
print(danh_sach_so)
ket_qua = timGiaTriTrungBinh(danh_sach_so)
print(f"Giá trị trung bình của các phần tử trong danh sách là {ket_qua}")
