#Search for pair of elements, summary of which equals value input by user
import random
n = input("Input random range, more than 0: ")
n = int(n)
lst = [random.randint(1, n) for _ in range(n // 2)]
print("List is: ", lst)
s = input("Input summary of 2 elements to search: ")
for i1 in range(n // 2):
    for i2 in range(i1+1, (n // 2)):
        if lst[i1] == int(s) - lst[i2]:
            print(s, "Is the summary of elements No.", i1, "and", i2)
            exit()
    if i1 == n // 2 - 1:
        print("There's no pair of elements to mach the input summary")
