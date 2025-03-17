from collections import defaultdict

def parse_filesystem(file_path):
    filesystem = defaultdict(list)
    current_path = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("$ cd "):
                dir_name = line[5:]
                if dir_name == "/":
                    current_path = ["/"]
                elif dir_name == "..":
                    if len(current_path) > 1:
                        current_path.pop()
                else:
                    current_path.append(dir_name)
            elif line.startswith("$ ls"):
                continue 
            else:
                parts = line.split()
                if parts[0] == "dir":
                    dir_name = parts[1]
                    filesystem["/".join(current_path)].append(("/".join(current_path + [dir_name]), 0))
                else:
                    file_size = int(parts[0])
                    file_name = parts[1]
                    filesystem["/".join(current_path)].append((file_name, file_size))
    return filesystem


def calculate_directory_sizes(filesystem):
    dir_sizes = {}
    def get_size(dir_path):
        if dir_path in dir_sizes:
            return dir_sizes[dir_path]
        total_size = 0
        for item, size in filesystem.get(dir_path, []):
            if size == 0:
                total_size += get_size(item)
            else:
                total_size += size
        dir_sizes[dir_path] = total_size
        return total_size
    get_size("/")
    return dir_sizes

file_path = "input_4.txt"
filesystem = parse_filesystem(file_path)
directory_sizes = calculate_directory_sizes(filesystem)
total_size_under_limit = sum(size for size in directory_sizes.values() if size <= 100000)
print("Total size of directories:", total_size_under_limit)