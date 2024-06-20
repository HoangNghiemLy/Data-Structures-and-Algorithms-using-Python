#Viết chương trình nhập một chuỗi vào từ bàn phím và đưa ra màn hình chuỗi đó nhưng viết theo thứ tự ngược lại
def daoNguocChuoi(chuoi):
    return chuoi[::-1]
chuoi = input("Nhập chuỗi cần đảo ngược: ")
print(f"Chuỗi sau khi đảo ngược là {daoNguocChuoi(chuoi)}")
