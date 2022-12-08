from itertools import islice

total_calories = [0]
individual_calories = [ [] ]
with open("input.txt") as data:
    elf = 0
    for line in data:
        if line == '\n':
            elf += 1
            total_calories.append(0)
            individual_calories.append([])
            continue
        else:
            calorie = int(line.strip())
            total_calories[elf] += calorie
            individual_calories[elf].append(calorie)

# solution 1
print(max(total_calories))

# solution 2
print(sum(islice(sorted(total_calories, reverse=True), 3)))