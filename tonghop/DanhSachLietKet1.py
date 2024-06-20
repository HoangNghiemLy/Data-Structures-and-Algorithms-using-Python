import os
import math as mt
import numpy as np
#các node của dslk đơn
class NODE:
    def __init__(self, data):
        self.data = data
        self.pNext = None

#pHead quản lý danh sách liên kết đơn
pHead = None

def snt(x):
    for i in range(2, int(mt.sqrt(x))+1 ):
        if x%i==0:
            return False
        
    if x>1: return True
    return False
#4 5 6 4 4 4 7 

#lớp danh sách liên kết đơn
class linked_list:
    #xóa node đầu.
    def xoaNodeDau():
        global pHead
        tmp = pHead
        pHead = pHead.pNext
        del tmp
    #xóa node cuối.
    def xoaNodeCuoi():
        global pHead
        tmp = pHead
        while tmp != None:
            if tmp.pNext.pNext == None:
                tmp1 = tmp.pNext
                tmp.pNext = None
                del tmp1
            tmp = tmp.pNext
    #thêm vào đầu node.
    def themVaoDau(x):
        global pHead
        x1= NODE(x)
        if pHead is None:
            pHead = x1
        else:
            x1.pNext = pHead
            pHead = x1
    #thêm vào cuối node.
    def themVaoCuoi(x):
        global pHead
        x1 = NODE(x)
        if pHead is None:
            pHead = x1
        else:
            tmp = pHead
            while tmp is not None:
                if tmp.pNext is None:
                    tmp.pNext = x1
                    break
                tmp = tmp.pNext
    #thêm vào sau 1 node có trước.
    def themVaoSauMotNode(p, x):
        global pHead
        if pHead is None:
            return
        else:
            tmp = pHead
            while tmp != None:
                if tmp.data == p:
                    x1 = NODE(x)
                    x1.pNext = tmp.pNext
                    tmp.pNext = x1
                    tmp = tmp.pNext
                tmp = tmp.pNext
    #thêm vào trước 1 node có trước .
    def themVaoTruocMotNode(p, x):
        global pHead
        if pHead is None: 
            return
        else:
            tmp = pHead
            if pHead.data == p:
                x1 = NODE(x)
                x1.pNext = pHead
                pHead = x1
    
            while tmp is not None:
                if tmp.pNext != None and tmp.pNext.data == p:
                    x1 = NODE(x)
                    x1.pNext = tmp.pNext
                    tmp.pNext = x1  
                    tmp = tmp.pNext
                tmp = tmp.pNext
    # xóa node bất kỳ
    def xoaNodeBatKy(id):
        global pHead
        if pHead == None:
            return
        dem = 0
        while  pHead != None and pHead.data == id :
            tmp = pHead
            pHead = pHead.pNext
            del tmp
        
        tmp1 = pHead
        while tmp1 != None:
            while tmp1.pNext!=None and tmp1.pNext.data == id:
                dem += 1
                i = tmp1.pNext
                tmp1.pNext = i.pNext
                del i
            tmp1 = tmp1.pNext
    #in danh sách liên kết
    def inDanhSach():
        tmp = pHead
        while tmp != None:
            print(str(tmp.data) + " ", end= "")
            tmp = tmp.pNext

    def tongCacSoTrongDanhSach():
        tmp = pHead
        sum = 0
        while tmp != None:
            sum += tmp.data
            tmp = tmp.pNext
        return sum
    
    def nhoNhat():
        tmp = pHead
        sum = 10000000
        while tmp != None:
            if sum < tmp.data: sum = tmp.data
            tmp = tmp.pNext
        return sum
    
    def lonNhat():
        tmp = pHead
        sum = -10000000
        while tmp != None:
            if sum > tmp.data: sum = tmp.data
            tmp = tmp.pNext
        return sum
    
    def BubbleSort1():
        global pHead
        tmp = pHead
        while(tmp is not None):
            tmp1 = tmp.pNext
            while(tmp1 is not None):
                if tmp1.data > tmp.data:
                    tmp1.data, tmp.data = tmp.data, tmp1.data
                tmp1 = tmp1.pNext
            tmp = tmp.pNext

    def BubbleSort2():
        global pHead
        tmp = pHead
        while(tmp is not None):
            tmp1 = tmp.pNext
            while(tmp1 is not None):
                if tmp1.data < tmp.data:
                    tmp1.data, tmp.data = tmp.data, tmp1.data
                tmp1 = tmp1.pNext
            tmp = tmp.pNext

    def danhSachCacPhanTuCoGiaTriChan():
        tmp = pHead
        while tmp != None:
            if tmp.data%2==0: print(str(tmp.data) + " ", end= "")
            tmp = tmp.pNext

    def timPhanTu(x):
        tmp = pHead
        while tmp != None:
            if tmp.data==x: return 1
            tmp = tmp.pNext
        return 0
    
    def inDSNguoc():
        tmp = pHead
        num = np.array([])
        while tmp!=None:
            num = np.append(num,tmp.data)
            tmp = tmp.pNext
        
        for i in range(np.size(num)-1, -1, -1):
            print(str(int(num[i])) + " ", end="")

    def tim_gia_tri_dau_tien_lon_hon_x(x):
        tmp = pHead
        while tmp != None:
            if(tmp.data > x): return tmp.data
            tmp = tmp.pNext
        return 0
    
    def xuat_snt_cuoi_cung():
        tmp = pHead
        s = 0
        while tmp!=None:
            if (snt(tmp.data)): s = tmp.data
            tmp=tmp.pNext
        return s
    
    def dem_snt():
        tmp = pHead
        dem = 0
        while tmp != None:
            if(snt(tmp.data)): dem+=1
            tmp=tmp.pNext

    def kiem_tra_tang_dan():
        tmp = pHead
        while tmp != None:
            if (tmp.pNext!=None and tmp.data > tmp.pNext.data):
                return 0
            tmp = tmp.pNext
        return 1
    
    def kiemTraDoiXung():
        if pHead==None: return
        tmp = pHead
        mang = np.array([])
        while tmp != None:
            mang = np.append(mang,tmp.data)
            tmp = tmp.pNext
        n=np.size(mang)
        for i in range(0, (np.size(mang)//2)+1,1):
            if(mang[n-i-1] != mang[i]):
                return 0
        return 1
            



while True:
    os.system("cls")
    print("\n\n\t\t---------------- MENU -----------------", end="")
    print("\n\t1. thêm vào đầu", end="")
    print("\n\t2. thêm vào cuối", end="")
    print("\n\t3. thêm vào trước một node cho trước", end="")
    print("\n\t4. thêm vào sau một node cho trước", end="")
    print("\n\t5. in thông tin danh sách", end="")
    print("\n\t6. xóa node bất kỳ.", end = "")
    print("\n\t7. Tổng giá trị của các số trong danh sách.",end="") 
    print("\n\t8. Giá trị lớn nhất trong danh sách", end='')
    print("\n\t9. Giá trị nhỏ nhất trong danh sách", end='')
    print("\n\t10. Sắp xếp Danh sách theo thứ tự tăng dần", end='')
    print("\n\t11. Sắp xếp Danh sách theo thứ tự giảm dần",end='')
    print("\n\t12. Danh sách các phần tử có giá trị là chẵn",end='')
    print("\n\t13. Tìm 1 phần tử có giá trị X trong danh sách",end='')
    print("\n\t14. In danh sach nguoc",end="")
    print("\n\t15. Xuất các số là số nguyên tố.", end='')
    print("\n\t16. Tìm giá trị đầu tiên lớn hơn x", end='')
    print("\n\t17. Kiểm tra mảng đối xứng.", end='')
    print("\n\t18. Kiếm tra tăng dần.")
    print("\n\t19. Xuất ")
    print("\n\n\t\t---------------------------------------", end="")
    n = int(input("\n\tNhập lựa chọn bạn muốn (nhập 0 để thoát): "))
    if n == 1:
        h = int(input("Nhập số bạn muốn thêm vào: "))
        linked_list.themVaoDau(h)
    elif n == 2:
        h = int(input("Nhập số bạn muốn thêm vào: "))
        linked_list.themVaoCuoi(h)
    elif n == 3:
        h = int(input("Nhập số bạn muốn thêm vào: "))
        j = int(input("Nhập số bạn muốn thêm vào trước số đó: "))
        linked_list.themVaoTruocMotNode(j, h)
    elif n == 4:
        h = int(input("Nhập số bạn muốn thêm vào: "))
        j = int(input("Nhập số bạn muốn thêm vào sau số đó: "))
        linked_list.themVaoSauMotNode(j, h)
    elif n == 5:
        linked_list.inDanhSach()
        print()
        input("Nhấn enter để tiếp tục !!!")
    elif n == 6:
        k = int(input("Nhập số bn muốn xóa: "))
        linked_list.xoaNodeBatKy(k)

    elif n == 7:
        sum = linked_list.tongCacSoTrongDanhSach()
        print("Tổng: " + str(sum))
        input("Nhấn enter để tiếp tục !!!")
    elif n==8:
        max = linked_list.lonNhat()
        print("max: " + str(max))
        input("Nhấn enter để tiếp tục !!!")
    elif n==9:
        min = linked_list.nhoNhat()
        print("min: " + str(min))
        input("Nhấn enter để tiếp tục !!!")
    elif n==10:
        linked_list.BubbleSort2()
        linked_list.inDanhSach()
        input("Nhấn enter để tiếp tục !!!")
    elif n==11:
        linked_list.BubbleSort1()
        linked_list.inDanhSach()
        input("Nhấn enter để tiếp tục !!!")
    elif n == 12:
        linked_list.danhSachCacPhanTuCoGiaTriChan()
        input("Nhấn enter để tiếp tục !!!")
    elif n== 13:
        n = int(input("Tìm phần tử: "))
        print(linked_list.timPhanTu(n))
        input("Nhấn enter để tiếp tục !!!")
    elif n==14:
        linked_list.inDSNguoc()
        input("Nhấn enter để tiếp tục !!!")
    elif n == 15:
        tmp = pHead
        while tmp!=None:
            if(snt(tmp.data)): print(str(tmp.data) + " ", end='')
            tmp = tmp.pNext
        input("Nhấn enter để tiếp tục !!!")
    elif n == 16:
        k = int(input("Nhập k: "))
        cc = linked_list.tim_gia_tri_dau_tien_lon_hon_x(k)
        print("Gía trị đầu tiên lớn hơn " + str(k) + "là: " + str(cc))
        input("Nhấn enter để tiếp tục !!!")
    elif n==17:
        if(linked_list.kiemTraDoiXung()!=0):
            print("Danh sách liên kết đang đối xứng !!!")
        else:
            print("Danh sách liên kết đang không đối xứng !!!")
        input("Nhấn enter để tiếp tục !!!")
    elif n==18:
        if(linked_list.kiem_tra_tang_dan()):
            print("mảng đang tăng dần !!!")
        else:
            print("Mảng không tăng dần !!!")
    elif n == 0:
        print("Chương trình kết thúc !!!")
        break
    else:
        input("Bạn đã nhập sai yêu cầu Nhấn enter để tiếp tục !!!")