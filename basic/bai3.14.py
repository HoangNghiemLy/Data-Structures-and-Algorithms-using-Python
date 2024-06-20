#Viết chương trình tim số Fibonacci thứ n
def timSoFibonacciThuN(n):
    if n <= 1:
        return n
    return timSoFibonacciThuN(n-1) + timSoFibonacciThuN(n-2)

n = int(input("Nhập số n: "))
print(f"Số Fibonacci thứ {n} là {timSoFibonacciThuN(n)}")
