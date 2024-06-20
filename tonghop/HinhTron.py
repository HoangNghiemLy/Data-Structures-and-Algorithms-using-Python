'''
Cài đặt lớp hình tròn theo thiết kế:
Có 1 fields: radius
Có các phương thức:
TÍnh diện tích ( area)
Tính chu vi (perimeter)
Hiển thị cơ bản (display)
Phạm vi khai báo class Circle được tính từ phím tab sau class Circle

'''
import math 
class Circle:
    #Hàm method khởi tạo (Constructor)
    def  __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pow(self.radius,2)*math.pi
    def perimeter(self):
        return self.radius*2*math.pi
    def display(self):
        print(f'Bán kính: {self.radius}, chu vi: {self.perimeter():.2f}, diện tích: {self.area():.2f}\n')
        
