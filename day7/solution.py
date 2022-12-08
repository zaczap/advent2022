from dataclasses import dataclass
from typing import List
from pprint import pprint

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    directories: dict
    files: List

root = Directory("", {"/": Directory("/", {}, []) }, [])
working_dir = [root]

with open("input.txt") as data:
    lines = [line.strip() for line in data.readlines()]
    current_line = 0
    
    while current_line < len(lines):
        # is the line a command?
        if lines[current_line].startswith('$'):
            # if so, buffer until the next command:
            command = lines[current_line].split(' ')[1:]
            output = []     
            while current_line + 1 < len(lines) and not lines[current_line + 1].startswith('$'):
                output.append(lines[current_line + 1])
                if current_line + 1 < len(lines):
                    current_line += 1
                else:
                    break
            
            # execute command:
            # print(command)
            # print(output)

            if command[0] == "cd":
                if command[1] == "..":
                    working_dir.pop()
                else:
                    working_dir.append(working_dir[-1].directories[command[1]])
            if command[0] == "ls":
                for entry in output:
                    field, name = entry.split(' ')
                    if field == "dir":
                        new_directory = Directory(name, {}, [])
                        working_dir[-1].directories[name] = new_directory
                    else:
                        size = int(field)
                        working_dir[-1].files.append(File(name, size))
            
        current_line += 1


def recursive_discovery(node, route = ""):
    # base 
    direct_size = sum(file.size for file in node.files)
    indirect_size = 0
    recording = {}
    if len(node.directories) == 0:
        pass
    else:
        for child_name, child_node in node.directories.items():
            total_size, subrecording = recursive_discovery(child_node, f"{route}/{child_name}")
            recording.update(subrecording)
            indirect_size += total_size
    total_size = direct_size + indirect_size
    recording[f"{route}/"] = total_size
    return total_size, recording

total_size, recording = recursive_discovery(root.directories["/"], "")

cumulative_sum = 0
for route, size in recording.items():
    if size <= 100000:
        cumulative_sum += size

print(cumulative_sum) # part 1

hard_drive_capacity = 70000000
total_space_needed = 30000000
hard_drive_used = total_size
space_remaining = hard_drive_capacity - hard_drive_used
space_to_be_freed = total_space_needed - space_remaining

min_waste = 100000000
winner = ""
for route, size in recording.items():
    if size > space_to_be_freed:
        waste = size - space_to_be_freed
        if waste < min_waste:
            min_waste = waste
            winner = route

print(recording[winner]) # part 2