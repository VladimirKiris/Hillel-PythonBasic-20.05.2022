#Finding square root of x, 0 <= x <= (2 ** 31) - 1
def sq_rt(x):
    top = x + 1
    low = 0
    mid = top // 2
    while True:
        mid = (top + low) // 2
        if mid ** 2 < x and (mid + 1) ** 2 > x:
            break
        if mid ** 2 > x:
            top = mid
        elif mid ** 2 < x:
            low = mid
        else:
            break
    return mid
a = input("Input number to check square root: ")
a = int(a)
print("Square root of",a, "is", sq_rt(a))