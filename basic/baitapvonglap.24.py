#Viết chương trình sắp xếp một list gồm các chuỗi theo thứ tự từ điển
def sapXepChuoi(list):
    list.sort()
    return list
list = ["ly","hoang","nghiem"]
print(list)
print(f"Danh sách mới sau khi sắp xếp là {sapXepChuoi(list)}")
