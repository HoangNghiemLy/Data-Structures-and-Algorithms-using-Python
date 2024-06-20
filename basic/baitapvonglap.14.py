#Viết chương trình tạo một bảng cửu chương từ 1 đến 10 theo cột
def bangCuuChuong():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")
        print("\n")
bangCuuChuong()

