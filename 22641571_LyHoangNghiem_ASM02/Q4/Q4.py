#------------------------------------------------------------
def gcd(n, m):
    # Write your statements here
    #.....
    gcd_result = 1
    min_value = min(n, m)
    for i in range(1, min_value + 1):
        if n % i == 0 and m % i == 0:
            gcd_result = i
    return gcd_result
    # End your statements
#end gcd
# ------------------------------------------------------------
def lcm(n, m):
    # Write your statements here
    lcm_result = (n*m) // gcd(n, m)
    return lcm_result
    # End your statements
#end lcm
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
def main():
    print("TEST Q4 (3 marks):")
    n = int(input("Enter n = "))
    m = int(input("Enter m = "))
    g = gcd(n, m);
    l = lcm(n, m);
    print("OUTPUT:")
    print(f"{g} ; {l}");
#=============================================================
#=============DO NOT ADD NEW OR CHANGE THIS STATEMENTS========
if __name__ == "__main__":
    main()
#=============================================================