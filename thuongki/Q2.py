import math
# --------------------------
def sum(n):
    # Write your statements here
    sum = 0
    for i in range(1,n+1):
        sum+=math.sqrt(i)
    return sum

    # End your statements
# end sum
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    print("TEST Q2 (3 marks):");
    n = int(input("Enter a number : "))
    result = sum(n)
    print("OUTPUT:")
    print(f"{result:0.2f}")
# end main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
