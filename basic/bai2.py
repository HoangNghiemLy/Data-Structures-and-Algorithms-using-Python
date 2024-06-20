#Các kiểu dữ liệu List, Tuple
#Kiểu dữ liệu danh sách: LIST
#Đây là kiểu dữ liệu có khả năng chứa nhiều phần tử khác nhau 
#Kể cả khác kiểu dữ liệu
listA = ['red',100,'blue',5.5,"yellow",2+4j]
print(listA)
#Có đánh chỉ số dương lẫn âm
print(listA[2])
print(listA[-2])
#Kết quả trả về của việc lấy theo một dãy các phần tử chỉ số
#Trong danh sách cũng là danh sách
#--> Được gọi là kỹ thuật SLICE
subListA = listA[2:5]
print(subListA)
print(subListA[1])
print(listA[1:-2])

#Đếm số lượng phần tử của danh sách
soluongpt = len(listA)
print(soluongpt)
print(len(listA))
#Lấy phần tử cuối cùng trong list
print(listA[-1]) #Lấy theo chỉ số âm
print(listA[soluongpt-1]) #Lấy theo chỉ số dương