directories = {}
cur_directory_stack = [directories]

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()
    if parts[0] == "$" and parts[1] == "cd":
        if parts[2] == "/":
            cur_directory_stack = [directories]
        elif parts[2] == "..":
            cur_directory_stack.pop()
        else:
            if parts[2] not in cur_directory_stack[-1]:
                cur_directory_stack[-1][parts[2]] = {}
            cur_directory_stack.append(cur_directory_stack[-1][parts[2]])
    elif parts[0] != "$":
        if parts[0] == "dir":
            if parts[1] not in cur_directory_stack[-1]:
                cur_directory_stack[-1][parts[1]] = {}
        else:
            size = int(parts[0])
            name = parts[1]
            cur_directory_stack[-1][name] = size


def dir_size(directory, target):
    total_size = 0
    for key, value in directory.items():
        if type(value) == int:
            total_size += value
        else:
            total_size += dir_size(value, target)
    if total_size <= 100000:
        target[0] += total_size
    return total_size


target_val = [0]

dir_size(directories, target_val)
print(target_val[0])