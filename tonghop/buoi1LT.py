#tính tổng các số lẻ từ 1 đến n bằng ngôn ngữ tự nhiên:
# Input: n
# Output: tong cac so le tu 1 den n
#B1: tong = 0
#B2: i=1
#B3: Nếu i>n thì sang B7, ngược lại sang B4
#B4: S=S+i
#B5: i=i+2
#B6: Quay lại B3
#B7: Hiển thị tong 



#tinh tong cac so le tu 1 den n
n = int(input("Nhap n ="))
tong = 0
for i in range(1,n+1, 2):
    tong += i
print(f"Tong cac so le tu 1 den {n} la: {tong}")