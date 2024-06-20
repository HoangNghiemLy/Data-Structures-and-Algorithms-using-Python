#Viết chương trình đổi một số nhị phân sang hệ thập phân
def doiSoNhiPhanSangThapPhan(n):
    return int(n,2)
n = input("Nhập số nhị phân cần đổi: ")
print(f"Số thập phân tương ứng là {doiSoNhiPhanSangThapPhan(n)}")