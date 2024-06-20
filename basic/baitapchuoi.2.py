#Viết chuong trình nhập hai chuỗi bất kì từ bàn phím và kiểm tra kí tự đầu tiên của 
#chuỗi thứ nhất có giống với kí tự cuối cùng của chuỗi thứ hai không
def kiemTraChuoi(chuoi1,chuoi2):
    if chuoi1[0] == chuoi2[-1]:
        return True
    else:
        return False
def main():
    chuoi1 = input("Nhập chuỗi thứ nhất: ")
    chuoi2 = input("Nhập chuỗi thứ hai: ")
    if kiemTraChuoi(chuoi1,chuoi2):
        print("Kí tự đầu tiên của chuỗi thứ nhất giống kí tự cuối cùng của chuỗi thứ hai")
    else:
        print("Kí tự đầu tiên của chuỗi thứ nhất không giống kí tự cuối cùng của chuỗi thứ hai")
if __name__ == "__main__":
    main()
     