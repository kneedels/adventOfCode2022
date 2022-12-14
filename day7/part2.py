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


def dir_size(directory, dir_sizes):
    total_size = 0
    for key, value in directory.items():
        if type(value) == int:
            total_size += value
        else:
            total_size += dir_size(value, dir_sizes)
    dir_sizes.append(total_size)
    return total_size


dir_sizes = []

total_size = dir_size(directories, dir_sizes)
avail_space = 70000000 - total_size
to_free = 30000000 - avail_space

dir_sizes.sort()

for size in dir_sizes:
    if size >= to_free:
        print(size)
        break

