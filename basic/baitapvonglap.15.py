#Viết chương trình tìm các từ độ dài lớn nhất trong một câu
def timTuDaiNhatTrongCau(cau):
    tu = cau.split(" ")
    tuDaiNhat = tu[0]
    for i in tu:
        if len(i) > len(tuDaiNhat):
            tuDaiNhat = i
        return tuDaiNhat
cau = input("Nhập câu: ")
print(f"Từ dài nhất trong câu là: {timTuDaiNhatTrongCau(cau)}")