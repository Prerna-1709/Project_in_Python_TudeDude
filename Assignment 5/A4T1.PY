

try :
    with open("sample.txt","rt") as fh :
        line1 = fh.readline().rstrip()
        line2 = fh.readline().rstrip()
    fh.close()
except FileNotFoundError  :
     print("Error : The file 'sample.txt' does not exist'")

else :
      print("Reading file content:")
      print(f"Line 1 :{line1}")
      print(f"Line 2 :{line2}")

