#Viết chuong trình tạo một list mới chỉ chứa các phần tử không trùng lặp list ban đầu
def taoListMoi(list):
    listMoi = []
    for i in list:
        if i not in listMoi:
            listMoi.append(i)
    return listMoi

list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4]
print(list)
print(f"Danh sách mới chỉ chứa các phần tử không trùng lặp là {taoListMoi(list)}")
