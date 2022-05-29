#kindergarden
group_a = int(input('input group "a" capacity:  '))
group_b = int(input('input group "b" capacity:  '))
beds = (group_a // 2 + (group_a % 2) + (group_b // 2 ) + group_b % 2)
print('we will need ', beds, "beds")
#sdads