with open("sample.txt", "r") as file:
    lines = file.readlines()


rope = [(0, 0) for _ in range(0, 10)]

visited = {(0, 0)}

print(f"Tail visits: (0, 0)")

iters = {"R": lambda pos: (pos[0] + 1, pos[1]),
         "L": lambda pos: (pos[0] - 1, pos[1]),
         "U": lambda pos: (pos[0], pos[1] - 1),
         "D": lambda pos: (pos[0], pos[1] + 1)}


def show_ropes(ropes):
    for row in range(0,5):
        for col in range(-0, 6):
            found_rope = False
            for i in range(0, len(ropes)):
                if rope[i] == (col, row):
                    print(i, end="")
                    found_rope = True
                    break
            if not found_rope:
                print(".", end="")
        print()




for line in lines:
    parts = line.split()
    direction = parts[0]
    amount = int(parts[1])
    iterator = iters[direction]
    for _ in range(0, amount):
        prev_knot = rope[0]
        rope[0] = iterator(rope[0])

        #print(f"Head moves from {prev_knot} to {rope[0]}")
        for i in range(1, len(rope)):
            last_knot_x, last_knot_y = rope[i-1]
            knot_x, knot_y = rope[i]
            if abs(knot_x - last_knot_x) > 1 or abs(knot_y - last_knot_y) > 1:
                new_prev_knot = rope[i]
                rope[i] = prev_knot
                #print(f"Knot {i} moves from {new_prev_knot } to {rope[i]}")
                prev_knot = new_prev_knot
                if i == len(rope) - 1:
                    visited.add(rope[i])
                    #print(f"Tail visits: {rope[i]}")
            else:
                break
        print(rope)
        show_ropes(rope)
        print()
    print("CD")

print(len(visited))
