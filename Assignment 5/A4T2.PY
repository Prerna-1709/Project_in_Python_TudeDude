with open("output.txt","wt") as fh:
    line1 = input("Enter text to write to the file :")
    fh.write(line1+ "\n")
    print("Data successfully written to output.txt.")
    fh.close()
with open("output.txt","at") as fh:
    line2 = input("Enter additional text to append :")
    print(" Data successfully appended.")
    fh.write(line2)
    fh.close()
with open("output.txt","rt") as fh:
    line3 = fh.read()
    print("Final content of output.txt:")
    print(line3)
    fh.close()


