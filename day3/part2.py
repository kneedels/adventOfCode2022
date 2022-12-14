with open("input.txt", "r") as file:
    lines = file.readlines()

encountered_chars = set()
total_score = 0


def get_index(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a')
    else:
        return ord(char) - ord('A') + 26


for group in zip(lines[::3], lines[1::3], lines[2::3]):
    common_items = None
    for line in group:
        line = line.strip()
        if common_items is None:
            common_items = set(line)
        else:
            common_items = common_items.intersection(set(line))
    total_score += get_index(common_items.pop()) + 1

print(total_score)
