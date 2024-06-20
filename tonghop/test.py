import os

class BanPhim:
    def __init__(self, ma,hang,ten,mausac,gia ):
        self.ma = ma
        self.hang = hang
        self.ten = ten
        self.mausac = mausac
        self.gia = gia

    def getMa(self):
        return self.ma
    def setMa(self,ma):
        self.ma = ma

    def getHang(self):
        return self.hang
    def setHang(self,hang):
        self.hang = hang

    def getTen(self):
        return self.ten
    def setTen(self,ten):
        self.ten = ten

    def getMauSac(self):
        return self.mausac
    def setMauSac(self,mausac):
        self.mausac = mausac

    def getGia(self):
        return self.gia
    def setGia(self,gia):
        self.gia = gia

    def hienthi(self):
        return f"Ma: {self.ma}, Hang: {self.hang}, Ten: {self.ten}, Mau sac: {self.mausac}, Gia: {self.gia}"
    

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linked_List:
    def __init__(self):
        self.pHead = None
    def isEmpty(self):
        return self.pHead == None
    def addQueue(self,x):
        if self.isEmpty():
            self.pHead = Node(x)
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.next is None:
                    tmp.next = Node(x)
                    break
                tmp = tmp.next
    def removeEnQueue(self):
        if self.isEmpty():
            return None
        else:
            tmp = self.pHead
            self.pHead = tmp.next
            return tmp.data
    def removeQueueEnd(self):
        if self.isEmpty():
            return None
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.next.next is None:
                    tmp.next = None
                    break
                tmp = tmp.next
    def removeQueueMa(self,ma):
        if self.isEmpty():
            return None
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.data.getMa() == ma:
                    tmp = tmp.next
                    break
                tmp = tmp.next
    def display(self):
        tmp = self.pHead
        while tmp != None:
            print(tmp.data.hienthi())
            tmp = tmp.next
    def search(self,ma):
        tmp = self.pHead
        while tmp != None:
            if tmp.data.getMa() == ma:
                return tmp.data.hienthi()
            tmp = tmp.next
        return None
    def sortMa(self):
        tmp = self.pHead
        while tmp != None:
            tmp1 = tmp.next
            while tmp1 != None:
                if tmp.data.getMa() > tmp1.data.getMa():
                    tmp.data,tmp1.data = tmp1.data,tmp.data
                tmp1 = tmp1.next
            tmp = tmp.next
class Stack:
    def __init__(self):
        self.pHead1 = None
    def isEmpty(self):
        return self.pHead1 == None
    def push(self,data):
        if data.getMa() % 2 == 0:
            if self.isEmpty():
                self.pHead1 = Node(data)
            else:
                tmp = self.pHead1
                while tmp != None:
                    if tmp.next is None:
                        tmp.next = Node(data)
                        break
                    tmp = tmp.next
    def display(self):
        tmp = self.pHead1
        while tmp != None:
            print(tmp.data.hienthi())
            tmp = tmp.next
l= Linked_List()
a=Stack()
l.addQueue(BanPhim(1,"Logitech","G213","Den",1000000))
l.addQueue(BanPhim(2,"Razer","Blackwidow","Den",2000000))
l.addQueue(BanPhim(3,"Corsair","K70","Den",3000000))
l.addQueue(BanPhim(4,"Steelseries","Apex","Den",4000000))
l.addQueue(BanPhim(5,"HyperX","Alloy","Den",5000000))

while True:
    os.system('cls')
    print("1. Them ban phim")
    print("2. Xoa ban phim")
    print("3. Tim kiem ban phim")
    print("4. Sap xep ban phim")
    print("5. Hien thi ban phim")
    print("6. Them ban phim vao stack")
    print("7. Hien thi stack")
    print("8. Thoat")
    n = int(input("Nhap lua chon: "))
    if n == 1:
        ma = int(input("Nhap ma: "))
        hang = input("Nhap hang: ")
        ten = input("Nhap ten: ")
        mausac = input("Nhap mau sac: ")
        gia = int(input("Nhap gia: "))
        l.addQueue(BanPhim(ma,hang,ten,mausac,gia))
    elif n == 2:
        ma = int(input("Nhap ma ban phim can xoa: "))
        l.removeQueueMa(ma)
    elif n == 3:
        ma = int(input("Nhap ma ban phim can tim: "))
        print(l.search(ma))
        input("Enter de tiep tuc")
    elif n == 4:
        l.sortMa()
    elif n == 5:
        l.display()
        input("Enter de tiep tuc")
    elif n == 6:
        ma = int(input("Nhap ma: "))
        hang = input("Nhap hang: ")
        ten = input("Nhap ten: ")
        mausac = input("Nhap mau sac: ")
        gia = int(input("Nhap gia: "))
        a.push(BanPhim(ma,hang,ten,mausac,gia))
    elif n == 7:
        a.display()
        input("Enter de tiep tuc")
    elif n == 8:
        break
    else:
        print("Nhap sai, nhap lai")
        input("Enter de tiep tuc")
        
