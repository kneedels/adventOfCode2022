with open('input.txt', 'r') as file:
    lines = file.readlines()

stack_count = int(len(lines[0]) / 4)
stacks = [[] for i in range(stack_count)]

for i, line in enumerate(lines):
    if line[1] == "1":
        break
    else:
        line_chars = line[1::4]
        for j, char in enumerate(line_chars):
            if char != " ":
                stacks[j].append(char)

for stack in stacks:
    stack.reverse()

for line in lines[i+2::]:
    parts = line.split()
    count = int(parts[1])
    from_stack = int(parts[3]) - 1
    to_stack = int(parts[5]) - 1
    for j in range(count):
        element = stacks[from_stack].pop()
        stacks[to_stack].append(element)

for stack in stacks:
    print(stack[-1], end="")