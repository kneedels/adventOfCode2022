with open("input.txt", "r") as file:
    lines = file.readlines()

line = lines[0].strip()

i = 0
j = 0

while i <= len(line):
    if i - j == 14:
        break
    else:
        k = j
        while k < i:
            if line[k] == line[i]:
                j = k + 1
                break
            k += 1
    i += 1

print(i)
