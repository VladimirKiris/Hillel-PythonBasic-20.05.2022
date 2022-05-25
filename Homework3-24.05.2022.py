#number inverter
n = int(input("input number  "))
a = n // 100
b = (n // 10) % 10
c = n % 10
d = c * 100 + b * 10 + a
print ('inverted number is ', d)