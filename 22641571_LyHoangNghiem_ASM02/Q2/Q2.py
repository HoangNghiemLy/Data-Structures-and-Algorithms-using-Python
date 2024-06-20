def sum(n):
    # Write your statements here
    #.......
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

    # End your statements
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
def main():
    print("TEST Q2 (3 marks):")
    n = int(input("Enter n = "))
    result = sum(n)
    print("OUTPUT:")
    print(result)
#============================================================
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == "__main__":
    main()
#============================================================

