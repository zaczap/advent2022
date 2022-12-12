from dataclasses import dataclass
from collections import deque
from typing import Callable, List
from functools import partial, reduce
from math import floor
from copy import deepcopy
import sys
from pprint import pprint

@dataclass
class Monkey:
    items: deque
    operation: Callable
    divisor: int
    true_target: int
    false_target: int

def add_op(operand, value = 0): 
    if value == "old":
        return operand + operand
    return operand + int(value)

def mul_op(operand, value = 0): 
    if value == "old":
        return operand * operand
    return operand * int(value)

monkeys = []

with open("input.txt") as data:
    lines = [line.strip() for line in data.readlines()]
    n_monkeys = (len(lines) + 1) // 7
    for i in range(n_monkeys):
        description = lines[(i*7):(i*7 + 6)]
        items = [int(x.strip()) for x in description[1].split(':')[1].strip().split(',')]
        operation = description[2].split(':')[1].strip().split(' ')[-2:]
        if operation[0] == '+': operation = partial(add_op, value = operation[1])
        elif operation[0] == '*': operation = partial(mul_op, value = operation[1])
        divisor = int(description[3].split(' ')[-1])
        true_target = int(description[4].split(' ')[-1])
        false_target = int(description[5].split(' ')[-1])
        monkeys.append(
            Monkey(deque(items), operation, divisor, true_target, false_target)
        )

monkey_backup = deepcopy(monkeys)

inspections = [0]*len(monkeys)

for round in range(20):
    for i in range(len(monkeys)):
        while len(monkeys[i].items) > 0:
            inspections[i] += 1
            item = monkeys[i].items.popleft()
            new_value = floor(monkeys[i].operation(item) / 3)
            if new_value % monkeys[i].divisor == 0:
                monkeys[monkeys[i].true_target].items.append(new_value)
            else:
                monkeys[monkeys[i].false_target].items.append(new_value)

# part 1
print(reduce(lambda x, y: x*y, sorted(inspections)[-2:]))

monkeys = monkey_backup

lcm = reduce(lambda x, y: x*y, [2, 3, 5, 7, 11, 13, 17, 19])

inspections = [0]*len(monkeys)

for round in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i].items) > 0:
            inspections[i] += 1
            item = monkeys[i].items.popleft()
            new_value = floor(monkeys[i].operation(item) % lcm)
            if new_value % monkeys[i].divisor == 0:
                monkeys[monkeys[i].true_target].items.append(new_value)
            else:
                monkeys[monkeys[i].false_target].items.append(new_value)

# part 2
print(reduce(lambda x, y: x*y, sorted(inspections)[-2:]))
