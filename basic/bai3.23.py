#Viết chương trình tính tiền điện hàng tháng của một hộ gia đình. Người sử dụng sẽ nhập số kWh từ bàn phím (là một số nguyên). Tiền điện được tính như sau: Nếu số KhW nhỏ hơn bằng 100 thì đơn giá là 2000 VNĐ. Nếu số KWh vượt 100, thì đơn giá cho mỗi KWh sẽ được cộng dồn thêm 100 VNĐ
def tinhTienDien(kwh):
    if kwh <=100:
        return kwh *2000
    else:
        return 100*2000 + (kwh-100)*2100
kwh = int(input("Nhập số KWh: "))
print(f"Số tiền điện hàng tháng là {tinhTienDien(kwh)}")


