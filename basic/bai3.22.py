#Nhập vào một chuỗi ký tự, nhập ký tự cần tìm. 
#In ký tự đó xuất hiện bao nhiêu lần tại vị trí nào và cho biết chiều dài chuỗi ký tự nhập vào
def timKiemChuoi(chuoi,kyTu):
    list = []
    for i in range(len(chuoi)):
        if chuoi[i] == kyTu:
            list.append(i)
    return list
chuoi = input("Nhập chuỗi: ")
kyTu = input("Nhập ký tự cần tìm: ")
list = timKiemChuoi(chuoi,kyTu)
print(f"Ký tự {kyTu} xuất hiện {len(list)} lần tại các vị trí {list} trong chuỗi {chuoi}")