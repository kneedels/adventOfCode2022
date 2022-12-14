import re

with open("input.txt", "r") as file:
    lines = file.readlines()

pattern = r"(?P<elf1_start>\d+)-(?P<elf1_end>\d+),(?P<elf2_start>\d+)-(?P<elf2_end>\d+)"
regex = re.compile(pattern)

overlaps = 0

for line in lines:
    match = regex.search(line)
    elf1 = (int(match.group("elf1_start")), int(match.group("elf1_end")))
    elf2 = (int(match.group("elf2_start")), int(match.group("elf2_end")))
    if elf1[0] <= elf2[0] <= elf1[1] or elf2[0] <= elf1[0] <= elf2[1]:
        overlaps += 1

print(overlaps)

