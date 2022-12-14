with open("input.txt", "r") as file:
    lines = file.readlines()

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0

visited = {(tail_x, tail_y)}

iters = {"R": lambda pos: (pos[0] + 1, pos[1]),
         "L": lambda pos: (pos[0] - 1, pos[1]),
         "U": lambda pos: (pos[0], pos[1] - 1),
         "D": lambda pos: (pos[0], pos[1] + 1)}

for line in lines:
    parts = line.split()
    direction = parts[0]
    amount = int(parts[1])
    iterator = iters[direction]
    for _ in range(0, amount):
        prev_head_x, prev_head_y = head_x, head_y
        head_x, head_y = iterator((head_x, head_y))
        if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
            tail_x, tail_y = prev_head_x, prev_head_y
            visited.add((tail_x, tail_y))

print(len(visited))
