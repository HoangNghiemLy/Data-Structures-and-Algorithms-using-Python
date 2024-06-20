#Viết chương trình sắp xếp một list gồm các số dương trước, tiếp theo là các số âm
def sapXepDuongAm(list):
    listDuong = []
    listAm = []
    for i in list:
        if i > 0:
            listDuong.append(i)
        else:
            listAm.append(i)
    return listDuong + listAm
list = [-2,-5,-6,1,3,2,5,6,-2,-10,-15]
print(list)
print(f"Danh sách mới sau khi sắp xếp là {sapXepDuongAm(list)}")

