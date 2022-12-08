
outcomes = {
    'A': {'X': 3, 'Y': 6, 'Z': 0}, # Rock
    'B': {'X': 0, 'Y': 3, 'Z': 6}, # Paper
    'C': {'X': 6, 'Y': 0, 'Z': 3}  # Scissors
}

personal_choice = {'X': 1, 'Y': 2, 'Z': 3}

end_score = {'X': 0, 'Y': 3, 'Z': 6}

hand_choice = {
    'A': {'X': 3, 'Y': 1, 'Z': 2}, # Rock
    'B': {'X': 1, 'Y': 2, 'Z': 3}, # Paper
    'C': {'X': 2, 'Y': 3, 'Z': 1}  # Scissors
}

cumulative_score = 0
corrected_cumulative_score = 0
with open("input.txt") as data:
    for line in data:
        moves = line.strip().split(' ')
        a, b = moves[0], moves[1]
        # solution 1
        score = outcomes[a][b] + personal_choice[b]
        cumulative_score += score
        # solution 2
        score = end_score[b] + hand_choice[a][b]
        corrected_cumulative_score += score

print(cumulative_score)
print(corrected_cumulative_score)