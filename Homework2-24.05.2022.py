#kindergarden
group_a = input('input group "a" capacity:  ')
group_b = input('input group "b" capacity:  ')
    #, input(int(group_a))
beds = (int(group_a) // 2 + 1) + (int(group_b) // 2 + 1)
print('we will need ', beds, "beds")
