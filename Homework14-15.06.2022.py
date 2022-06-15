#Finding square root of x, 0 <= x <= (2 ** 31) - 1
def sq_rt(x):
    lst = list(range(0,x+1))
    while True:
        l = len(lst)
        m = l // 2
        if l == 1:
            lst = lst[0]
            break
        if lst[m] ** 2 > x:
            lst = lst[0 : m]
        elif lst[m] ** 2 < x:
            lst = lst[m: l]
        else:
            lst = lst[m]
            break
    return lst
a = input("Input number to check square root: ")
a = int(a)
print("Square root of",a, "is", sq_rt(a))