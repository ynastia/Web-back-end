def read_input_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def extract_calibration_value(line):
    digits = [char for char in line if char.isdigit()]
    if digits:
        return int(digits[0] + digits[-1])
    return 0

file_path = "input_3.txt"
lines = read_input_file(file_path)

total_calibration_sum = sum(extract_calibration_value(line) for line in lines)

print("Total Calibration Sum:", total_calibration_sum)