import copy

with open("input.txt") as data:
    data = [line.strip() for line in data]

pivot = data.index('')
stacks = data[0:(pivot-1)]
buckets = {k.strip(): [] for k in data[pivot-1].split('  ')}
moves = data[(pivot+1):]

indices = dict(zip(map(str, range(1,10)), [2*i for i in range(9)]))
for stack in stacks[::-1]:
    stack = stack.replace('[','').replace(']','').replace('  ', ' ')
    for label, index in indices.items():
        if index > len(stack): 
            continue
        else:
            if stack[index] != ' ':
                buckets[label].append(stack[index])

buckets_backup = copy.deepcopy(buckets)

for move in moves:
    _, n, _, source, _, dest = move.split(' ')
    for x in range(int(n)):
        buckets[dest].append(buckets[source].pop())

message = []
for label, stack in buckets.items():
    message.append(stack[-1])

print("".join(message))

### Part 2

buckets = buckets_backup

for move in moves:
    _, n, _, source, _, dest = move.split(' ')
    uprooted = [buckets[source].pop() for x in range(int(n))]
    buckets[dest].extend(uprooted[::-1])

message = []
for label, stack in buckets.items():
    message.append(stack[-1])

print("".join(message))

