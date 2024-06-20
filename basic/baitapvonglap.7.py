#Viết chương trình tìm số chẵn cuối cùng trong một list 
def timSoChanCuoiCungTrongList(list):
    for i in list[::-1]:
        if i % 2 == 0:
            return i
        
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(f"Số chẵn cuối cùng trong danh sách là {timSoChanCuoiCungTrongList(list)}")