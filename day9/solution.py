from dataclasses import dataclass

@dataclass
class Cell:
    row: int
    col: int

    def slide(self, direction):
        if direction == "U": 
            self.row += 1
        elif direction == "D":
            self.row -= 1
        elif direction == "R":
            self.col += 1
        elif direction == "L":
            self.col -= 1

origin = Cell(0,0)
head = Cell(0,0)
tail = Cell(0,0)

# .X.X. 
# X...X 
# ..T..
# X...X
# .X.X.
    
def slither(head, tail):
    if head.row == tail.row and head.col == tail.col: return tail # same position
    
    if head.row - 1 == tail.row and head.col == tail.col: return tail # head is directly U
    if head.row == tail.row and head.col - 1 == tail.col: return tail # head is directly R
    if head.row == tail.row and head.col + 1 == tail.col: return tail # head is direclty L
    if head.row + 1 == tail.row and head.col == tail.col: return tail # head is direclty D

    if head.row - 1 == tail.row and head.col - 1 == tail.col: return tail # head is U+R
    if head.row - 1 == tail.row and head.col + 1 == tail.col: return tail # head is directly U+L
    if head.row + 1 == tail.row and head.col + 1 == tail.col: return tail # head is directly D+R
    if head.row + 1 == tail.row and head.col - 1 == tail.col: return tail # head is directly D+L
    
    # head is further away (follow or slither to match rank)
    if head.row - 1 > tail.row and head.col == tail.col: # head is up 2
        tail.slide("U") 
        return tail
    elif head.row + 1 < tail.row and head.col == tail.col: # head is down 2
        tail.slide("D")
        return tail
    elif head.row == tail.row and head.col - 1 > tail.col: # head is right 2
        tail.slide("R")
        return tail
    elif head.row == tail.row and head.col + 1 < tail.col: # head is left 2
        tail.slide("L")
        return tail
    elif head.row - 2 == tail.row:
        if head.col + 1 == tail.col:
            tail.slide("U")
            tail.slide("L")
            return tail
        elif head.col - 1 == tail.col:
            tail.slide("U")
            tail.slide("R")
            return tail
    elif head.row - 1 == tail.row:
        if head.col + 2 == tail.col:
            tail.slide("U")
            tail.slide("L")
            return tail
        elif head.col - 2 == tail.col:
            tail.slide("U")
            tail.slide("R")
            return tail
    elif head.row + 2 == tail.row:
        if head.col + 1 == tail.col:
            tail.slide("D")
            tail.slide("L")
            return tail
        elif head.col - 1 == tail.col:
            tail.slide("D")
            tail.slide("R")
            return tail
    elif head.row + 1 == tail.row:
        if head.col + 2 == tail.col:
            tail.slide("D")
            tail.slide("L")
            return tail
        elif head.col - 2 == tail.col:
            tail.slide("D")
            tail.slide("R")
            return tail

    # X...X
    # .....
    # ..T..
    # .....
    # X...X

    # double diagonals:
    if head.row - 2 == tail.row and head.col + 2 == tail.col:
        tail.slide("U")
        tail.slide("L")
        return tail
    if head.row - 2 == tail.row and head.col - 2 == tail.col:
        tail.slide("U")
        tail.slide("R")
        return tail
    if head.row + 2 == tail.row and head.col + 2 == tail.col:
        tail.slide("D")
        tail.slide("L")
        return tail
    if head.row + 2 == tail.row and head.col - 2 == tail.col:
        tail.slide("D")
        tail.slide("R")
        return tail

    raise ValueError("Tail became separated!", head, tail)


visited = set()

with open("input.txt") as moves:
    for slide in moves:
        direction, steps = slide.strip().split(' ')
        steps = int(steps)
        for step in range(steps):
            head.slide(direction)
            tail = slither(head, tail)
            visited.add((tail.row, tail.col))


# part 1; why does the origin not count?
print(len(visited))

visited = set()
knots = list(map(Cell, [0]*10, [0]*10))
with open("input.txt") as moves:
    for i, slide in enumerate(moves):
        direction, steps = slide.strip().split(' ')
        steps = int(steps)
        for step in range(steps):
            knots[0].slide(direction)
            for k in range(1, len(knots)):
                knots[k] = slither(knots[k-1], knots[k])
            visited.add((knots[-1].row, knots[-1].col))

# part 2
print(len(visited))