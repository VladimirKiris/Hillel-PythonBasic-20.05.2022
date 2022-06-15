#Reverse the dictionary

translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
print(translations)

rev_dict = {}
for key, val in translations.items():
   rev_dict[tuple(val)] = key
print("Reversed dictionary: ", rev_dict)
