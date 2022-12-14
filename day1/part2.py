import time

max_calories = [0] * 3
cur_calories = 0

with open("input.txt", 'r') as file:
    lines = file.readlines()

start_time = time.perf_counter_ns()

for line_num, line in enumerate(lines):
    line = line.strip()
    if len(line):
        cur_calories += int(line)
    if not len(line) or line_num == len(lines) - 1:
        min_of_maxes = min(max_calories)
        if min_of_maxes < cur_calories:
            for i, calories in enumerate(max_calories):
                if calories == min_of_maxes:
                    max_calories[i] = cur_calories
                    break
        cur_calories = 0


end_time = time.perf_counter_ns()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time / 1000000}ms")

print(sum(max_calories))

