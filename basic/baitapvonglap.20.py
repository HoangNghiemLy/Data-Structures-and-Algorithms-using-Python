#Viet chuong trình tìm số dư của một phép chia
def soDu(a,b):
    return a%b
def main():
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    print(f"Số dư của {a}/{b} là: {soDu(a,b)}")
if __name__ == "__main__":
    main()
     