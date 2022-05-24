#kindergarden
group_a = input('input group "a" capacity:  ')
group_b = input('input group "b" capacity:  ')
beds = (int(group_a) // 2 + (int(group_a) % 2) + (int(group_b) // 2 ) + int(group_b) % 2)
print('we will need ', beds, "beds")
