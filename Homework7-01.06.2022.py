# Sentence count in text
s = input("Input text: ")
if s.rfind(".") >= len(s)-2:
    print("Your text has", s.count("."), "sentences")
else:
    print("Your text has", s.count(".")+1, "sentences")