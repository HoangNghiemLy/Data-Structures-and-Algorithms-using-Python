#Cài đặt lớp hình chữ nhật theo thiết kế:
# Có 2 fields: width, height
#Có các phương thức:
#TÍnh diện tích ( area)
#Tính chu vi (perimeter)
#Hiển thị cơ bản (display)
#Phạm vi khai báo class Rectangle được tính từ phím tab sau class Rectangle

class Rectangle:
    #Hàm method khởi tạo (Constructor)
    #Đây là method đặc biệt phải có khi khai báo class
    #Mục đích: để nạp những giá trị ban đầu cho các thể hiện ( cụ thể)
    #Của đối tượng chương trình
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return (self.width + self.length)*2
    def display(self):
        print(f'Rộng: {self.width}, dài: {self.length}, chu vi: {self.perimeter():.2f}, diện tích: {self.area():.2f}\n')
        