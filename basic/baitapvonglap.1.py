#Bài tập vòng lặp
#tính tổng s= 0 +1 +..+n, trong đó n là số tự nhiên nhập từ bàn phím. Yêu cầu viết bằng for..range, while

def tinhTongFor(n):
    s = 0
    for i in range(n+1):
        s+=i
    return s
def tinhTongWhile(n):
    s = 0
    i = 0
    while i<=n:
        s+=i
        i+=1
    return s
n = int(input("Nhập n: "))
print(f"Tổng từ 0 đến {n} bằng vòng lặp for là {tinhTongFor(n)}")
print(f"Tổng từ 0 đến {n} bằng vòng lặp while là {tinhTongWhile(n)}")
