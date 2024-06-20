'''
Description: Các thuật toán sắp xếp
1. Interchange sort
input: day (a,n)
output: day da sap xep
-B1: i = 0
-B2: j = i+1
-B3: Trong khi j<n thực hiện:
--B3.1: Nếu a[i]>a[j] thì đổi chỗ a[i] và a[j]
--B3.2: j=j+1
-B4: i=i+1
-B5: Quay lại B2
-B6: Hiển thị day
'''

print("1. Interchange sort")
a = [6,5,3,1,8,7,2,4,9]
print("Mảng chưa sắp xếp:")
print(a)
def InterchangeSort(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n,1):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
print("Mảng sau khi sắp xếp:")
print(InterchangeSort(a))          
print("--------------------------------------------------")
print()


'''
2.Bubble Sort 
input: day (a,n)
output: day da sap xep
-B1: i = 0
-B2: j = n-1
-B3: Trong khi j>i thực hiện:
--B3.1: Nếu a[j]<a[j-1] thì đổi chỗ a[j] và a[j-1]
--B3.2: j=j-1
-B4: i=i+1
-B5: Quay lại B2
-B6: Hiển thị day
'''

print("2. Bubble Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp:")
print(a)
def BubbleSort(a):
    n=len(a)
    for i in range (n):
        for j in range(0,n-i-1,1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print("Mảng sau khi sắp xếp:")
print(BubbleSort(a))
print("--------------------------------------------------")
print()


'''
3.Insertion Sort
input: day (a,n)
output: day da sap xep 
-B1: i = 1
-B2: Trong khi i<n thực hiện:
--B2.1: x=a[i]
--B2.2: j=i-1
--B2.3: Trong khi j>=0 và a[j]>x thực hiện:
---B2.3.1: a[j+1]=a[j]
---B2.3.2: j=j-1
--B2.4: a[j+1]=x
--B2.5: i=i+1
-B3: Hiển thị day
'''

print("3. Insertion Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp:")
print(a)
def InsertionSort(a):
    n=len(a)
    for i in range(n):
        x=a[i]
        pos=i
        while pos>0 and x<a[pos-1]:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos]=x
    return a
print("Mảng sau khi sắp xếp:")
print(InsertionSort(a))
print("--------------------------------------------------")
print()


'''
4. Selection Sort
input: day (a,n)
output: day (a,n) da sap xep
-B1: i=0
-B2: Tìm phần tử a[min] nhỏ nhất trong dãy con a[i+1]...a[n-1]  
-B3: Hoán đổi a[i] và a[min]
-B4: i=i+1
-B5: Quay lại B2
-B6: Hiển thị day

'''
print("4. Selection Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp: ")
print(a)
def SelectionSort(a):
    n=len(a)
    for i in range(0,n-1,1):
        min=i
        for j in range(i+1,n,1):
            if a[j] < a[min]:
                min=j
        if min!=i:
            a[i],a[min]=a[min],a[i]
    return a
print("Mảng đã sắp xếp: ")
print(SelectionSort(a))
print("--------------------------------------------------")
print()

'''
5. Quick Sort
-B1: Nếu left = right
--B1.1: Kết thúc
-B2: Phân hoạch dãy a[left]....a[right] thành 3 đoạn:
--B2.1: a[left]....a[i] đoạn 1  
--B2.2: a[i+1]....a[j-1] đoạn 2
--B2.3: a[j]....a[right] đoạn 3
-B3: Gọi đệ quy QuickSort(a,left,i)
-B4: Gọi đệ quy QuickSort(a,j,right)
'''

print("5. Quick Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp: ")
print(a)
def partition(a,left,right):
    #Chọn phần tử bên phải cuối cùng làm phần tử pivot (phần tử chốt)
    pivot=a[right]
    #Con trỏ cho phần tử lớn hơn
    i=left - 1
    #Duyệt qua tất cả các phần tử và so sánh vơi phần tử pivot
    for j in range(left,right):
        if a[j] <= pivot:
            #Nếu phần tử nhỏ hơn pivot, thực hiện hoán đổi với phần tử lớn hơn được trỏ bởi i
            i+=1
            #Hoán đổi phần tử tại i với phần tử tại j
            a[i],a[j] = a[j],a[i]
    #Hoán đổi phần tử pivot với phần tử lớn hơn chỉ định bởi i
    a[i+1],a[right] = a[right],a[i+1]
    return i+1
#Hàm thực hiện sắp xếp QuickSort
def QuickSort(a,left,right):
    if left < right:
        #Tìm phần tử pivot sao cho phần tử pivot nằm bên trái và lớn hơn nằm bên phải
        pi = partition(a,left,right)
        #Gọi đệ quy hàm với phần bên trái của pivot
        QuickSort(a,left,pi-1)
        #Gọi đệ quy hàm với phần bên phải của pivot
        QuickSort(a,pi+1,right)
    return a
print("Mảng sau khi sắp xếp: ")
print(QuickSort(a,0,len(a)-1))
print("--------------------------------------------------")
print()


'''
6. Heap Sort
GD1: Hiệu chỉnh dãy số ban đầu thành heap
GD2: Sắp xêps dãy số dựa trên heap:
-B1: Hoán đổi phần tử đầu tiên với phần tử cuối cùng trong heap
-B2: Giảm kích thước heap đi 1
-B3: Hiệu chỉnh lại heap
-B4: Quay lại B1
'''
print("6. Heap Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp: ")
print(a)
def Heap_Sort(a,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and a[i] < a[left]:
        largest = left
    if right < n and a[largest] < a[right]:
        largest = right
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        Heap_Sort(a,n,largest)
def HeapSort(a):
    n = len(a)
    for i in range (n,-1,-1):
        Heap_Sort(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        Heap_Sort(a,i,0)
    return a
print("Mảng sau khi sắp xếp: ")
print(HeapSort(a))
print("--------------------------------------------------")
print()


'''
7. Merge Sort
input: day (a,n)
output: day (a,n) da sap xep
-B1: Nếu n=1
--B1.1: Kết thúc
-B2: Gọi đệ quy MergeSort(a,0,n/2)
-B3: Gọi đệ quy MergeSort(a,n/2+1,n)
-B4: Gọi hàm Merge(a,0,n/2,n)
-B5: Hiển thị day
'''
print("7. Merge Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp: ")
print(a)
def Merge_Sort(a):
    n = len(a)
    if n>1:
        mid = n//2
        left_half = a[:mid]
        right_half = a[mid:]
        #Đệ quy sắp xếp từng phần
        Merge_Sort(left_half)
        Merge_Sort(right_half)
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] =left_half[i]
                i+=1
            else:
                a[k] = right_half[j]
                j+=1
            k+=1
        while i < len(left_half):
            a[k] = left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            a[k] = right_half[j]
            j+=1
            k+=1
    return a

print("Mảng sau khi sắp xếp: ")
print(Merge_Sort(a))
print("--------------------------------------------------")
print()


'''
8. Shell Sort
input: day (a,n)
output: day (a,n) da sap xep
-B1: Chọn khoảng cách h
-B2: Chia dãy thành các nhóm con
-B3: Sắp xếp các nhóm con
-B4: Giảm khoảng cách h
-B5: Quay lại B2
-B6: Hiển thị day
'''

print("8. Shell Sort")
a = [6,5,2,7,8,9,1,3,4]
print("Mảng chưa sắp xếp: ")
print(a)
def ShellSort(a):
    n = len(a)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = a[i]
            j = i
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j-=gap
            a[j] = temp
        gap//=2
    return a
print("Mảng sau khi sắp xếp: ")
print(ShellSort(a))
print("--------------------------------------------------")
print()











        




        
    



