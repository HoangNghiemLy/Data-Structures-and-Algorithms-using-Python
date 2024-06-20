#Hãy nhập một số tự nhiên từ bàn phím sau đó, xuất màn hình thông báo số đó có phải là số nguyên tố hay không

def kiemTraSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
n = int(input("Nhập số cần kiểm tra: "))
if kiemTraSoNguyenTo(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")
