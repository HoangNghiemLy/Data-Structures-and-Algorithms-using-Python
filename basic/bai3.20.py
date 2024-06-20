#Viết chương trình giải phương trình bậc 1 ax+b=0, trong đó a,b là các số thực được nhập từ bàn phím
def giaiPhuongTrinhBac1(a,b):
    if a == 0:
        if b == 0:
            return False
        else:
            return True
    else:
        return -b/a
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if giaiPhuongTrinhBac1(a,b) == False:
    print(f"Phương trình {a}x+{b}=0 có vô số nghiệm")
elif giaiPhuongTrinhBac1(a,b) == True:
    print(f"Phương trình {a}x+{b}=0 vô nghiệm")
else:
    print(f"Phương trình {a}x+{b}=0 có nghiệm là {giaiPhuongTrinhBac1(a,b)}")