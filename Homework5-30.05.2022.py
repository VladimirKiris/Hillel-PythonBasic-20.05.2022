#Numbers sequence
sm = 0
count = 0
mx = 0
mn = 0
while True:
    x = input("Input int number: ")
    if not x:
        break
    else:
        sm += int(x)
        count += 1
        if int(mn) == 0 and int(mx) == 0:
            mn = x
            mx = x
        if int(x) > int(mx):
            mx = x
        if int(mn) > int(x):
            mn = x
print("Numbers input: ", count)
print("Summary of elements in the list: ", sm)
print("Max number: ", mx)
print("Min number: ", mn)
print("Average fm list: ", sm / count)