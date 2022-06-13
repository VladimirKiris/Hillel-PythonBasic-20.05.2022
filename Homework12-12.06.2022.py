#Counting words in text
text = str("В строке записан много слово. Для каждого слово из записан текста посчитайте, сколько раз слово встречалось, и выведите записан на экран. "
        "На 100 балов: выведите топ-5 самых используемых слово  Необходимо решить с помощью словаря слово.")
print(text)
to_remove = ['.',',',':','!','?','-']
new = filter(lambda c: c not in to_remove, text)
a = ""
for c in new:
    a += c
a = a.lower()
a = a.split(" ")
word_frq = {}
for i in a:
    if i in word_frq:
            word_frq[i] += 1
    else:
        word_frq[i] = 1
print(word_frq)
sorted_list = sorted(word_frq.items(), key=lambda el:el[1], reverse=True)
print("Top-5 words are: ", sorted_list[:5])
