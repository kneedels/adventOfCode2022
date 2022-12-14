with open("input.txt", "r") as file:
    lines = file.readlines()

encountered_chars = set()
total_score = 0


def get_index(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a')
    else:
        return ord(char) - ord('A') + 26


for line in lines:
    line = line.strip()
    for i, char in enumerate(line):
        if i < len(line) / 2:
            encountered_chars.add(char)
        elif char in encountered_chars:
            total_score += get_index(char) + 1
            break
    encountered_chars.clear()

print(total_score)
