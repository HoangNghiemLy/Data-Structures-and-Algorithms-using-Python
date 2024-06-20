#Viết chương trình đổi độ C sang độ F 
def doiDoCDoF(doC):
    return (doC *9/5) +32 
doC = float(input("Nhập độ C: "))
print(f"Độ F là {doiDoCDoF(doC)}")