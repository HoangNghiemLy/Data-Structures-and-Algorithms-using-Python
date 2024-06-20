#khởi tạo list chứa giá trị nhiệt độ 7 ngày trong tuần, giá trị nhiệt độ được nhập từ bàn phím
#tính nhiệt độ trung bình của tuần. Đếm xem có bao nhiêu ngày nhiệt độ lớn hơn trung bình

def nhapNhietDo():
    nhietDo = []
    for i in range(7):
        nhietDo.append(float(input(f"Nhập nhiệt độ ngày thứ {i+1}: ")))
    return nhietDo

def tinhNhietDoTrungBinh(nhietDo):
    return sum(nhietDo)/len(nhietDo)

def demSoNgayNhietDoLonHonNhietDoTrungBinh(nhietDo, nhietDoTrungBinh):
    dem = 0
    for i in nhietDo:
        if i > nhietDoTrungBinh:
            dem += 1
    return dem

nhietDo = nhapNhietDo()
nhietDoTrungBinh = tinhNhietDoTrungBinh(nhietDo)
print(f"Nhiệt độ trung bình của tuần là {nhietDoTrungBinh}")
print(f"Số ngày nhiệt độ lớn hơn nhiệt độ trung bình là {demSoNgayNhietDoLonHonNhietDoTrungBinh(nhietDo, nhietDoTrungBinh)}")
