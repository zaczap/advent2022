from collections import deque
from collections import namedtuple
import sys

with open("input.txt") as data:
    program = deque([x.strip() for x in data.readlines()])

cycle = 1
register = 1
signals = [0]

image = []

command = None

while len(program) > 0 or command:
    # print(f'Cycle #{cycle} - {register} - {command}')
    if (cycle - 1) % 40 == 0:
        image.append([])
    if register - 1 <= (cycle - 1) % 40 <= register + 1:
        image[-1].append('#')
    else:
        image[-1].append(' ')
    signals.append(cycle * register)
    if not command:
        command = program.popleft()
        if command.startswith('noop'):        
            command = None
            cycle += 1
            continue
        else:
            cycle += 1
            continue
    if command:
        _, value = command.split(' ')
        register += int(value)
        command = None
        cycle += 1

# clean up
signals.append(cycle * register)
# print(f'Cycle #{cycle} - {register} - {command}')

# part 1
indices = [20, 60, 100, 140, 180, 220]
print(sum(signals[i] for i in indices))

# part 2
for line in image:
    print("".join(line))