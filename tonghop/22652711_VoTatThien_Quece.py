import numpy as np

class NODE:
    def __init__(self, data):
        self.data = data
        self.pNext = None

class STACK:
    def __init__(self):
        self.pHead = None

    def IsEmpty(self):
        return self.pHead is None
    
    def themVaoStack(self, x):
        x1 = NODE(x)
        if self.pHead is None:
            self.pHead = x1
        else:
            x1.pNext = self.pHead
            self.pHead = x1
    
    def xoaDauStack(self): 
        if self.pHead is None: return
        tmp = self.pHead
        self.pHead = self.pHead.pNext
        del tmp

    def xemPhanTuDau(self):
        return self.pHead.data

class QUEUE:
    def __init__(self):
        self.pHead = None 
    
    def themVaoQueue(self, x):
        x1 = NODE(x)
        if self.pHead is None:
            self.pHead = x1
        else:
            tmp = self.pHead
            while tmp != None:
                if tmp.pNext == None:
                    tmp.pNext = x1
                    break
                tmp = tmp.pNext

    def xoaDauQueue(self):
        if self.pHead is None: return
        tmp = self.pHead
        self.pHead = self.pHead.pNext
        del tmp

    def xemPhanTuDauQueue(self):
        return self.pHead.data
    
    def inDanhSach(self):
        tmp = self.pHead
        print("Result: ", end='')
        while tmp != None:
            print(str(tmp.data) + " ", end = "")
            tmp = tmp.pNext

def doUuTienToanTu(x):
    if x == "+" or x == "-": return 1
    if x == "*" or x == "/": return 2
    if x == "^": return 3
    return -1

Stack1 = STACK()
Queue1 = QUEUE()

s = input("Nhập đa thức bất kỳ mà bạn muốn: ")



def TrungToSangHauTo(s):
    global Stack1, Queue1
    s = s.split(" ")
    for i in range(0, len(s)):
        if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/" or s[i] == "^":
            if Stack1.IsEmpty() == True:
                Stack1.themVaoStack(s[i])
            else:
                if(doUuTienToanTu(Stack1.xemPhanTuDau()) < doUuTienToanTu(s[i])):
                    Stack1.themVaoStack(s[i])
                else:
                    while Stack1.IsEmpty() == False and doUuTienToanTu(Stack1.xemPhanTuDau()) >= doUuTienToanTu(s[i]):
                        Queue1.themVaoQueue(Stack1.xemPhanTuDau())
                        Stack1.xoaDauStack()
                    Stack1.themVaoStack(s[i])
        elif s[i] == "(" or s[i] == ")":
            if s[i] == "(":
                Stack1.themVaoStack(s[i])
            else:
#Stack  )   +   (
#Queue  1   2
                while True:
                    if Stack1.xemPhanTuDau() == "(": break
                    Queue1.themVaoQueue(Stack1.xemPhanTuDau())
                    Stack1.xoaDauStack()
                Stack1.xoaDauStack()
        else:
            Queue1.themVaoQueue(s[i])

    while Stack1.IsEmpty() == False:
        Queue1.themVaoQueue(Stack1.xemPhanTuDau())
        Stack1.xoaDauStack()

TrungToSangHauTo(s)
Queue1.inDanhSach()