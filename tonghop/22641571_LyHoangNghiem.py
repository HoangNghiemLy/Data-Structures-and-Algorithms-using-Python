import os
class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value
    
    def info(self):
        return f"ID: {self.id}, Value: {self.value}"
    
class IdValueNode:
    def __init__(self,data):
        self.data = data
        self.pNext = None

class IdValueSLL:
    def __init__(self):
        self.pHead = None
        self.pTail = None
    
    def isEmpty(self):
        if self.pHead == None and self.pTail == None:
            return True
        else: return False
    
    def isDuplicated(self, id):
        tmp = self.pHead
        while tmp != None:
            if tmp.data.id == id:
                return True
            tmp = tmp.pNext
        return False
    
    def addTail(self, newData):
        tmp = IdValueNode(newData)
        if self.pHead == self.pTail == None:
            self.pHead = tmp
            self.pTail = tmp
        else:
            self.pTail.pNext = tmp
            self.pTail = tmp

    def traverse(self):
        tmp = self.pHead
        while tmp != None:
            print(tmp.data.info())
            tmp = tmp.pNext
a = IdValueSLL()
while True:
    os.system("cls")
    print("1. Them vao cuoi. ") 
    print("2. Check danh sach co rong khong. ")
    print("3. Tim kiem node. ")
    print("4. In danh sachh node. ")
    chon = int(input("Nhap lua chon: "))
    if chon == 1:
        id = input("Nhap id: ")
        value = int(input("Nhap so nguyen: "))
        id_value = IdValue(id, value)
        a.addTail(id_value)
    elif chon == 2:
        if a.isEmpty() == True:
            print("Danh sach dang rong !!!")
        else:
            print("Danh sach dang co phan tu !!!")
        input("Nhan enter de tiep tuc !!!")
    elif chon == 3:
        id = input("Nhap id ban muon tim: ")
        if a.isDuplicated(id) == True:
            print("YES")
        else:
            print("NO")
        input("Nhan enter de tiep tuc !!!")
    elif chon == 4:
        a.traverse()
        input("Nhan enter de tiep tuc !!!")
    elif chon==0:
        print("Ket thuc chuong trinh !!")
        break
    else:
        input("Nhap sai !!!")



        
    

        