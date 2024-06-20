#Viết hàm tính giá trị bình phương của một số sau đó, gọi hàm
def tinhBinhPhuong(n):
    return n**2
n = float(input("Nhập số cần tính bình phương: "))
print(f"Bình phương của {n} là {tinhBinhPhuong(n)}")
