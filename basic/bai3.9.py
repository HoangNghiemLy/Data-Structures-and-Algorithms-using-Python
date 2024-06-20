#Viết chương trình đổi độ F sang độ C
def doiDoFDoC(doF):
    return (doF - 32) * 5/9
doF = float(input("Nhập độ F:"))
print(f"Độ C là {doiDoFDoC(doF)}")