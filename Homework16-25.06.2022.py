# 2 ** n, 2 is given by user


def power(num: int) -> int | float:
    p = 2
    if num == 0:
        p = 1
    elif num < 0:
        for _ in range(abs(num) - 1):
            p *= 2
        p = 1 / p
    else:
        for _ in range(num - 1):
            p *= 2
    return p


def power_rec(num=int) -> int or float:
    p = 2
    if num == 0:
        p = 1
    elif num < 0:
        p = 1 / power_rec(abs(num))
    else:
        p *= power_rec(num - 1)
    return p


n = int(input("Enter n to get 2 ** n: "))
print("Loop calc 2 ** n =", power(n))
print("Recursive calc 2 ** n =", power_rec(n))
