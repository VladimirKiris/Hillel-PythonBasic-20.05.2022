#String Slicing etc
s = input("Input text: ")
print("Length of the text:", len(s))
print("Odd index Symbols:")
for i in range(len(s)):
    if (i-1) % 2 > 0:
        continue
    else: print(s[i], end=" ")
print("\nEven index Symbols:")
for i in range(len(s)):
    if (i-1) % 2 != 0:
        print(s[i], end=" ")
    else: continue
if len(s) >= 5 :
    print("\n5th Symbol is:", s[4])
print("Text to 10th (first 9) symbol:", s[:9])
print("Last 5 symbols:", s[len(s)-5:len(s)])
print("Reverse text:", s[::-1])
print("Reverse text with step 2:", s[::-2])
if s[::1] == s[::-1]:
    print ("Text is palindrome")
else:
    print("Text is non-palindrome")