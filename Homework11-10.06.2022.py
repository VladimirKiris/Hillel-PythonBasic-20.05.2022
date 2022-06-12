#unique names search
set_names = set()
set_repeat = set()
while True:
    a = input("Enter name to add it to the list then press Enter: ")
    if not a:
        break
    if a not in set_names:
        set_names.add(a)
    else:
        set_repeat.add(a)
print("Unique names are:", set_names - set_repeat)