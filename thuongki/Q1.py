import  math
#----------------------------------------------------------------
def isPrime(number):
    #Begin your statements here
    if number <2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i ==0:
            return False
    return True


    
    #End your statements
#end isPrime
#----------------------------------------------------------------
def average(x):
    # Begin your statements here
    primes_sum = 0
    count = 0
    i = 2
    while count < x:
        if isPrime(i):
            primes_sum += i
            count += 1
        i += 1
    return primes_sum / x

    #End your statements
#end average
#=============DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("\nTEST Q1 (2 marks):")
    x = int(input("Enter x = "))
    r = average(x)
    print("OUTPUT:")
    print("{:.2f}".format(r))
#end main
if __name__ == "__main__":
   main()
#====================================================================================
