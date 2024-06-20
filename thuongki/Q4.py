def countWord(fileName,str):
    # Write your statements here
    count = 0
    with open(fileName) as f:
        for line in f:
            for word in line.split():
                if word.lower().startswith(str.lower()):
                    count += 1
    return count
    #End your statements
#end averageNumbers
#========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
def main():
  print("TEST Q4 (3 marks):");
  fileName =  input("Enter file name : ")
  str = input("Enter string : ")
  result = countWord(fileName,str)
  print("OUTPUT:")
  print(f"{result}")
#end main
#--------------------------------
if __name__ == "__main__":
  main()
#============================================================
  




