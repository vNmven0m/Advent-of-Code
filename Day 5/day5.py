import math


def checkrule(update, rule):
    if rule[0] in update:
        for page in update:
            if page == rule[1]:
                return False
            if page == rule[0]:
                return True
    return True

def reorder_update(update, rules):
    reordered = False
    for rule in rules:
        if not checkrule(update,rule):
            idx_a = update.index(rule[0])
            idx_b = update.index(rule[1])
            update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
            reordered = True
    if reordered:
        update = reorder_update(update,rules)

    return update


rules = []
updates = []
result = result2 = 0

with open("Day 5/input/input.txt") as f:
    ruleread = True
    for line in f:
        if ruleread: 
            if line == '\n':
                ruleread = False
                continue
            x, y = line.strip().split("|")
            rules.append(tuple((int(x),int(y))))
            continue
        updates.append(list(map(int,(line.strip().split(",")))))


for update in updates:
    if all(checkrule(update,rule) for rule in rules):
        result += update[math.trunc(len(update)/2)]
        continue

    result2 += reorder_update(update, rules)[math.trunc(len(update)/2)]



print("Part 1:", result)
print("Part 2:", result2)