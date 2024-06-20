import  math
#------------------------------------------------------------
#The function used to check whether n is prime or not
def isPrime(n):
    # Write your statements here
    #...
    if n <=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    # End your statements
#end isPrime
# ------------------------------------------------------------
# The function used to print calculate and print the result
def calculate(n):
    # Write your statements here
    if isPrime(n):
        return n * n
    else:
        return n * 2
    # End your statements
#end calculate
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
def main():
    print("TEST Q3 (2 marks):")
    n = int(input("Enter n = "))
    result = calculate(n)
    print("OUTPUT:")
    print(result)
#=============================================================
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == "__main__":
    main()
#=============================================================