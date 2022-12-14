with open("input.txt", "r") as file:
    lines = file.readlines()

forest = [list(map(int, line.strip())) for line in lines]


def is_visible_internal(forest, position, height, iter):
    row, col = position
    if row < 0 or col < 0 or row >= len(forest) or col >= len(forest[row]):
        return True
    elif forest[row][col] >= height:
        return False
    else:
        return is_visible_internal(forest, iter(position), height, iter)


iters = [lambda position: (position[0], position[1] + 1),
         lambda position: (position[0], position[1] - 1),
         lambda position: (position[0] + 1, position[1]),
         lambda position: (position[0] - 1, position[1])]

def is_visible(forest, position):
    row, col = position
    for iter in iters:
        if is_visible_internal(forest, iter(position), forest[row][col], iter):
            return True
    return False

total_visible = 0

for row in range(0, len(forest)):
    for col in range(0, len(forest[row])):
        if is_visible(forest, (row, col)):
            total_visible += 1
            
print(total_visible)