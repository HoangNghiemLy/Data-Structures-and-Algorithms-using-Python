#Viết chương trình tìm các số lớn hơn trung bình của một list
def timSoLonHonTrungBinhCuaList(list):
    tong = 0
    for i in list:
        tong += i
    trungBinh = tong / len(list)
    listKetQua = []
    for i in list:
        if i > trungBinh:
            listKetQua.append(i)
    return listKetQua

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(f"Trung bình của list là {sum(list)/len(list)}")
print(f"Các số lớn hơn trung bình của danh sách là {timSoLonHonTrungBinhCuaList(list)}")

    