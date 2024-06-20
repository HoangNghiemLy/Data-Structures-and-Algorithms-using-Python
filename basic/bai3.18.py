#Viết chương trình kiểm tra xem một chuỗi có phải là chuỗi hợp lệ để biểu diễn một số nguyên hay không
def kiemTraChuoiHopLe(list):
    for i in list:
        if i not in "0123456789":
            return False
    return True
list = input("Nhập chuỗi cần kiểm tra: ")
if kiemTraChuoiHopLe(list):
    print(f"{list} là chuỗi hợp lệ để biểu diễn một số nguyên")
else:
    print(f"{list} không là chuỗi hợp lệ để biểu diễn một số nguyên")