#number inverter
n = input("input number  ")
a = int(n) // 100
b = (int(n) % 100 - int(n) % 10 ) / 10
c = int(n) % 10
d = round(c * 100 + b * 10 + a)
print ('inverted number is ', d)