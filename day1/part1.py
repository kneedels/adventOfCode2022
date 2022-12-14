max_calories = 0
cur_calories = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if not len(line):
            if cur_calories > max_calories:
                max_calories = cur_calories
            cur_calories = 0
        else:
            cur_calories += int(line)

print(max_calories)

