#Viết chương trình tìm các số chia hết cho 3 hoặc cho 5 trong một list
def timSoChiaHetCho3Hoac5(list):
    list_so_chia_het_cho_3_hoac_5 = []
    for i in list:
        if i % 3 == 0 or i % 5 == 0: 
            list_so_chia_het_cho_3_hoac_5.append(i)
    return list_so_chia_het_cho_3_hoac_5

danh_sach_so = [3,1,5,9,10,55,21]
print(danh_sach_so)
ket_qua = timSoChiaHetCho3Hoac5(danh_sach_so)
print(f"Các số chia hết cho 3 hoặc 5 trong danh sách là {ket_qua}")
