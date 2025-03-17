def read_strategy_guide(file_path):
    rounds = []
    with open(file_path, 'r') as file:
        for line in file:
            opponent, response = line.strip().split()
            rounds.append((opponent, response))
    return rounds

def calculate_score(rounds):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_score = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3 
    }
    total_score = 0
    for opponent, response in rounds:
        total_score += shape_score[response] + outcome_score[(opponent, response)]
    return total_score

file_path = "input_6.txt"
rounds = read_strategy_guide(file_path)
total_score = calculate_score(rounds)
print("Total Score:", total_score)