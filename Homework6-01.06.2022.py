# n replacement with N
s = input("Input text containing n: ")
b = s[:s.find(" ")]
e = s[s.rfind(" ") + 1:]
m = s[s.find(" ") + 1: s.rfind(" ")].replace("n", "N")
print(b, m, e)
