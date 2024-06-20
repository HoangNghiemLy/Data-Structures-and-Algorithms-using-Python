#IdValue Class
class IdValue:
    def __init__(self,id,value):
    #============================================================
    #BEGIN your statements here
        pass
    #END your statements
    #============================================================= 

    #=============================================================
    #DO NOT ADD NEW OR CHANGE THE STATEMENTS
    def info(self):
        return self.id+str(self.value)
    #END
    #=============================================================

#IdValue Node Class
class IdValueNode:
    def __init__(self, data, next):
    #============================================================
    #BEGIN your statements here
        pass
    #END your statements
    #=============================================================
    
    #=============================================================
    #DO NOT ADD NEW OR CHANGE THE STATEMENTS
    def info(self):
      if self.next != None:
        return self.data.info()+">"
      else:
        return self.data.info()+">null"  
    #END
    #=============================================================

#IdValue Single Linked List Class
class IdValueSLL:
    def __init__(self):
    #============================================================
    #BEGIN your statements here
        pass 
    #END your statements
    #=============================================================
           
    def isEmpty(self):
    #============================================================
    #BEGIN your statements here
        pass
    #END your statements
    #=============================================================

    def isDuplicated(self,_id):
    #============================================================
    #BEGIN your statements here
        pass
    #END your statements
    #============================================================
    
    def addTail(self, newdata):
    #============================================================
    #BEGIN your statements here
        pass
    #END your statements
    #=============================================================
        
    #=============================================================
    #DO NOT ADD NEW OR CHANGE THE STATEMENTS
    def checkResult(self):
        resultCode = "null"
        count = 0
        if self.isEmpty():
            return str(count)+resultCode
        current = self.head
        while current != None:
            count = count+1

            temp = current.info()
            if current.next != None:
                temp = temp + current.next.data.id +">"

            resultCode=resultCode+temp
            current = current.next
        return str(count)+resultCode
    #END

#==================================================================================
#DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION
def main():
    print("TEST Q1 (5 marks):")
    kvList = IdValueSLL()

    soluong = int(input("Input number of items:"))
    for i in range(soluong):                
        cod = input("Input id:")
        val = int(input("Input value:"))
        item = IdValue(cod,val)
        if kvList.isDuplicated(cod) == False:
            kvList.addTail(item)

    print("OUTPUT:")
    print(kvList.checkResult())
            
#END MAIN
if __name__ == '__main__':
    main()
#==================================================================================