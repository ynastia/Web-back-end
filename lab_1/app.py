def read_input_file(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    return total_distance

def calculate_similarity_score(left_list, right_list):
    right_count = {}
    for num in right_list:
        if num in right_count:
            right_count[num] += 1
        else:
            right_count[num] = 1
    similarity_score = 0
    for num in left_list:
        if num in right_count:
            similarity_score += num * right_count[num]
    return similarity_score

file_path = "input_1.txt"
left_list, right_list = read_input_file(file_path)
total_distance = calculate_total_distance(left_list, right_list)
similarity_score = calculate_similarity_score(left_list, right_list)
print("Total Distance:", total_distance)
print("Similarity Score:", similarity_score)