#Numbers sequence

a = []
while True:
    x = input("Input int number to list: ")
    if x == '':
        break
    else:
        a.append(int(x))
print("The list is: ", a)
print("Numbers in the list: ", len(a))
print("Summary of elements in the list: ", sum(a))
print("Max number: ", max(a))
print("Min number: ", min(a))
print("Average fm list: ", sum(a) / len(a))