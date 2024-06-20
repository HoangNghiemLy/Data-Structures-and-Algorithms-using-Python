#Viết hàm tính các phép tính số học (+,-,*,/) của hai số được nhập vào từ bàn phím
def tinhTong(a,b):
    return a+b
def tinhHieu(a,b):
    return a-b
def tinhTich(a,b):
    return a*b
def tinhThuong(a,b):
    return a/b
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
print(f"Tổng của {a} và {b} là {tinhTong(a,b)}")
print(f"Hiệu của {a} và {b} là {tinhHieu(a,b)}")
print(f"Tích của {a} và {b} là {tinhTich(a,b)}")
print(f"Thương của {a} và {b} là {tinhThuong(a,b)}")
