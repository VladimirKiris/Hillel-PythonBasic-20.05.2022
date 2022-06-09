#Search for Neighbour numbers in the random list, random range N, list length N/2
import random
n = input("Input random range, more than 0: ")
lst = [random.randint(1, int(n)) for _ in range((int(n) // 2))]
print("List is: ", lst)
s = input("Input number to search: ")
ch = False
for i, el in enumerate(lst):
    if el == int(s):
        ch = True
        print("Found in psn", i)
        if 0 < i < (int(n) // 2) - 1:
            print("Previous:", lst[i - 1], "Next:", lst[i + 1])
        elif i == 0:
            print("Next only available:", lst[i + 1])
        elif i == (int(n) // 2) - 1:
            print("Previous only available:", lst[i - 1])
if not ch:
    print("No such value")
