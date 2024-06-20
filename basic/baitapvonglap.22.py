#Viết chương trình tìm tất cả các số chính phương trong một list
def timSoChinhPhuong(list):
    so_chinh_phuong = []
    for i in list:
        if i > 0:
            if (i**0.5)%1 == 0:
                so_chinh_phuong.append(i)
    return so_chinh_phuong
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(f"Danh sách số chính phương là {timSoChinhPhuong(list)}")
