
fully_contained_count = 0
partially_overlap_count = 0

with open("input.txt") as data:
    for pairing in data:
        elements = pairing.strip().replace(',', ' ').replace('-', ' ').split(' ')
        min1, max1, min2, max2 = map(int, elements)
        if min1 <= min2 and max1 >= max2:
            fully_contained_count += 1
        elif min2 <= min1 and max2 >= max1:
            fully_contained_count += 1
        if min1 <= min2 and min2 <= max1:
            partially_overlap_count += 1
        elif min1 <= max2 and max2 <= max1:
            partially_overlap_count += 1
        elif min2 <= min1 and min1 <= max2:
            partially_overlap_count += 1
        elif min2 <= max1 and max1 <= max2:
            partially_overlap_count += 1

        
print(fully_contained_count)
print(partially_overlap_count)