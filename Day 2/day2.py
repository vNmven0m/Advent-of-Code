count = count2 = 0


def check_valid(report):
    if all((1 <= abs(report[i]-report[i+1]) <= 3) for i in range(len(report) -1 )) and (all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1))):
        return True
    return False


with open("Day 2/input/input") as f:
    for line in f:
        report = list(map(int,(line.strip().split(" "))))
        if check_valid(report):
            count += 1
            continue
        for i in range(len(report)):
            temp = report[:i] + report[i + 1:]
            if check_valid(temp):
                count2 += 1
                break
                

print("Part 1:", count)
print("Part 2:", count + count2)