#Viết chương trình đếm số từ trong một câu
def demSoTuTrongCau(cau):
    tu = cau.split(" ")
    return len(tu)
cau = input("Nhập câu: ")
print(f"Số từ trong câu là: {demSoTuTrongCau(cau)}")
