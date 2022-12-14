import heapq

calories_queue = []
cur_calories = 0

with open("input.txt", 'r') as file:
    lines = file.readlines()

for line_num, line in enumerate(lines):
    line = line.strip()
    if len(line):
        cur_calories += int(line)
    if not len(line) or line_num == len(lines) - 1:

        if len(calories_queue) < 3:
            heapq.heappush(calories_queue, cur_calories)
        elif cur_calories > calories_queue[0]:
            heapq.heapreplace(calories_queue, cur_calories)

        cur_calories = 0

print(sum(calories_queue))

