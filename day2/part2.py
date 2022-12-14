expected_outcomes = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}

winning_outcomes = {"A": "Y", "B": "Z", "C": "X"}
draw_outcomes = {"A": "X", "B": "Y", "C": "Z"}
losing_outcomes = {"A": "Z", "B": "X", "C": "Y"}
move_scores = {"X": 1, "Y": 2, "Z": 3}
outcome_scores = {"WIN": 6, "DRAW": 3, "LOSE": 0}

total_score = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.split()
        total_score += outcome_scores[expected_outcomes[parts[1]]]
        if expected_outcomes[parts[1]] == "WIN":
            total_score += move_scores[winning_outcomes[parts[0]]]
        elif expected_outcomes[parts[1]] == "DRAW":
            total_score += move_scores[draw_outcomes[parts[0]]]
        else:
            total_score += move_scores[losing_outcomes[parts[0]]]

print(total_score)