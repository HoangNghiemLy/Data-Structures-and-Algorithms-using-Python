def average(n):
    # Write your statements here
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("{:.2f}".format(sum/n))

    # End your statements
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
def main():
    print("TEST Q1 (2 marks):")
    n = int(input("Enter n = "))
    print("\nOUTPUT:")
    average(n)
#============================================================
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == "__main__":
    main()
#============================================================

