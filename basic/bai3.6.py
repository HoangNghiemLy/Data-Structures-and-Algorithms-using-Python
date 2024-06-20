#Viết chương trình đảo ngược một chuỗi
def daoNguocChuoi(chuoi):
    return chuoi[::-1]

chuoi = input("Nhập chuỗi cần đảo ngược: ")
print(f"Chuỗi sau khi đảo ngược là {daoNguocChuoi(chuoi)}")
