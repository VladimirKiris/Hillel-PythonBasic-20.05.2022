# Writing to file. Test program creates file, writes lines input by user, prints the file then deletes it.
import os

s = None
with open("Testfile.txt", "w") as file:
    while s != "":
        s = input("Add line to Testfile:")
        file.write("\n")
        file.write(s)
with open("Testfile.txt", "r") as file:
    print("file:", file.read())
    print("Test file will be deleted. Thanks")
os.remove("Testfile.txt")
