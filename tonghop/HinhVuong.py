class HinhVuong:
    def __init__(self, canh):
        self.canh = canh
    def chuvi(self):
        return self.canh * 4
    def dientich(self):
        return self.canh * self.canh
    def hienthi(self):
        print("Hinh vuong co canh la: ", self.canh)
        print("Chu vi hinh vuong la: ", self.chuvi())
        print("Dien tich hinh vuong la: ", self.dientich())