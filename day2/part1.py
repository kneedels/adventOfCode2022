move_map = {"X": "A", "Y": "B", "Z": "C"}
winning_outcomes = {"X": "C", "Y": "A", "Z": "B"}
move_scores = {"X": 1, "Y": 2, "Z": 3}
outcome_scores = {"WIN": 6, "DRAW": 3, "LOSE": 0}

total_score = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.split()
        total_score += move_scores[parts[1]]
        if move_map[parts[1]] == parts[0]:
            total_score += outcome_scores["DRAW"]
        elif winning_outcomes[parts[1]] == parts[0]:
            total_score += outcome_scores["WIN"]
        else:
            total_score += outcome_scores["LOSE"]

print(total_score)