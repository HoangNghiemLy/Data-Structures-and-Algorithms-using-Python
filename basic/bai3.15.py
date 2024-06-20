#Viết chương trình sắp xếp một list theo thứ tự tăng dần
def sapXepTangDan(list):
    list.sort()
    return list
list = [8,10,1,2,3,5,0,-1]
print(f"Danh sách ban đầu là {list}")
print(f"Danh sách sau khi sắp xếp là {sapXepTangDan(list)}")
