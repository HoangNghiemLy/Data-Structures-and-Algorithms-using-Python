#Viết chương trình kiểm tra xem một chuỗi có phải là palindrome hay không
def kiemTraPalindrome(list):
    if list == list[::-1]:
        return True
    return False
list = input("Nhập chuỗi cần kiểm tra: ")
if kiemTraPalindrome(list):
    print(f"{list} là chuỗi palindrome")
else:
    print(f"{list} không là chuỗi palindrome")