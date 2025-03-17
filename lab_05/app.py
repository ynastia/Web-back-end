def read_games(file_path):
    games = []
    with open(file_path, 'r') as file:
        for line in file:
            game_id_part, subsets_part = line.strip().split(": ")
            game_id = int(game_id_part.split()[1])
            subsets = subsets_part.split("; ")
            game_data = []
            for subset in subsets:
                cube_counts = {"red": 0, "green": 0, "blue": 0}
                colors = subset.split(", ") 
                for color_entry in colors:
                    count, color = color_entry.split()
                    cube_counts[color] = int(count)
                game_data.append(cube_counts)
            games.append((game_id, game_data))
    return games
def is_game_possible(game_data, max_cubes):
    for subset in game_data:
        if subset["red"] > max_cubes["red"] or subset["green"] > max_cubes["green"] or subset["blue"] > max_cubes["blue"]:
            return False
    return True

file_path = "input_5.txt"
games = read_games(file_path)
max_cubes = {"red": 12, "green": 13, "blue": 14}
sum_possible_game_ids = sum(game_id for game_id, game_data in games if is_game_possible(game_data, max_cubes))
print("Sum of Possible Game IDs:", sum_possible_game_ids)