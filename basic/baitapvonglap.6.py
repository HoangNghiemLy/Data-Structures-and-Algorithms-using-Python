#Viết chuong trình tính tổng các số lẻ trong một list dùng vòng lặp
def timSoLe(list):
    listLe = []
    for i in list:
        if i %2!=0:
            listLe.append(i)
    return listLe
def tongSoLe(list):
    tong = 0
    for i in list:
        if i %2!=0:
            tong += i
    return tong
list = [1,2,3,4,5,6,7,8,9,10]
print(f"Các số lẻ trong danh sách {timSoLe(list)}")
print(f"Tổng các số lẻ trong danh sách là {tongSoLe(list)}")