#Fibonacci calculation. F(0) = 0, F(1) = 1; F(n) = F(n - 1) + F(n - 2), for n > 1.
#F(8) = 21 (sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21)


def fib_loop(number: int) -> int:
    f_first = 0
    f_sec = 1
    for i in range(0, number+1):
        if i <= 1:
            fib = i
        else:
            fib = f_first + f_sec
            f_first = f_sec
            f_sec = fib
    return fib

def fib_rec(number: int) -> int:
    if number == 0:
        fib = 0
    elif number == 1:
        fib = 1
    else:
        fib = fib_rec(number - 2) + fib_rec(number - 1)
        print(fib)
    return fib

number = int(input("Input Number to get Fibonacci F(n): "))
print("Loop F(",number,") = ", fib_loop(number))
print("Recursion F(",number,") = ", fib_rec(number))