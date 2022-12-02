with open('input1.txt') as f:
    arrayRaw = f.readlines()
caloreis4elves = [ [int(y) for y in x.split('\n')] for x in "".join(arrayRaw).split('\n\n')]
total_calories = [sum(x) for x in caloreis4elves]

# ## Solution 1
# Elv1 = max(total_calories)
# print(max(total_calories))

# total_calories[total_calories.index(Elv1)] = 0
# Elv2 = max(total_calories)
# total_calories[total_calories.index(Elv2)] = 0
# Elv3 = max(total_calories)
# print(Elv1+Elv2+Elv3)

## Solution 2 
total_calories.sort(reverse =True)
print(total_calories[0])
print(sum(total_calories[0:3]))