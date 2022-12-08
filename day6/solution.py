with open("input.txt") as data:
    data = data.readlines()[0].strip()

for i in range(len(data)-3):
    n_distinct = len(set(data[i:(i+4)]))
    if n_distinct == 4:
        print(i+4)
        break

for i in range(len(data)-13):
    n_distinct = len(set(data[i:(i+14)]))
    if n_distinct == 14:
        print(i+14)
        break