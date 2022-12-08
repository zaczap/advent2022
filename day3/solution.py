import itertools

priorities = dict(zip(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1,53)))

cumulative_sum = 0
with open("input.txt") as rucksacks:
    for sack in rucksacks:
        sack = sack.strip()
        n = len(sack)
        bin1, bin2 = sack[0:(n//2)], sack[(n//2):]
        assert len(bin1) == len(bin2)
        overlap = set(bin1) & set(bin2)
        assert len(overlap) == 1
        cumulative_sum += priorities[list(overlap)[0]]

print(cumulative_sum)

cumulative_sum = 0
with open("input.txt") as rucksacks:
    rucksacks = tuple(rucksacks)
    bag1 = itertools.islice(rucksacks, 0, None, 3)
    bag2 = itertools.islice(rucksacks, 1, None, 3)
    bag3 = itertools.islice(rucksacks, 2, None, 3)
    for elf1, elf2, elf3 in zip(bag1, bag2, bag3):
        elf1 = elf1.strip()
        elf2 = elf2.strip()
        elf3 = elf3.strip()
        overlap = set(elf1) & set(elf2) & set(elf3)
        cumulative_sum += priorities[list(overlap)[0]]

print(cumulative_sum)
