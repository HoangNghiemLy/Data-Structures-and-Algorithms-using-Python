class sort:
    def interchangeSort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n,1):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
    
    def bubbleSort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1,1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
    def insertionSort(self,arr):
        
                
