with open("input.txt", "r") as file:
    lines = file.readlines()

forest = [list(map(int, line.strip())) for line in lines]


def get_directional_visibility(forest, position, height, iter):
    row, col = position
    if row < 0 or col < 0 or row >= len(forest) or col >= len(forest[row]):
        return 0
    elif forest[row][col] >= height:
        return 1
    else:
        return 1 + get_directional_visibility(forest, iter(position), height, iter)


iters = [lambda position: (position[0], position[1] + 1),
         lambda position: (position[0], position[1] - 1),
         lambda position: (position[0] + 1, position[1]),
         lambda position: (position[0] - 1, position[1])]

def visibility_score(forest, position):
    score = 1
    row, col = position
    for iter in iters:
        score *= get_directional_visibility(forest, iter(position), forest[row][col], iter)
    return score

max_visibility = 0

for row in range(0, len(forest)):
    for col in range(0, len(forest[row])):
        score = visibility_score(forest, (row, col))
        if score > max_visibility:
            max_visibility = score

print(max_visibility)