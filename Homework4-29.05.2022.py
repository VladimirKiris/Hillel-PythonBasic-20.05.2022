# Prime Numbers check
# prime row first 25: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
import time
a = int(input("Number check for Prime. \nInput positive int number: "))
if a <= 1: exit("negative number, 0 or 1!!")
start_time = time.time()
for check in range(2, a):
    if a % check == 0:
        print("Your number ", a, " is composite")
        break
else:
    print("\nYour number ", a, " is prime")
print("Prime row before ", a, " is")
for check in range(2, a):
    for p_list in range(2, check):
        if check % p_list == 0:
            break
    else:
        print(check, end=", ")

print("Executed in %s seconds " % (time.time() - start_time))