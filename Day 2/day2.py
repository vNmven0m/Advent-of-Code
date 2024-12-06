count = count2 = 0

with open("Day 2\input\input") as f:
    for line in f:
        report = list(map(int,(line.strip().split(" "))))
        if all((1 <= abs(report[i]-report[i+1]) <= 3) for i in range(len(report) -1 )) and (all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1))):
            count += 1
            continue
        if all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1)) and 0 <= len(report)-len(list(dict.fromkeys(report))) <= 1:
            dis = []
            for i in range(len(report)-1):
                dis.append(report[i]-report[i+1])
            print(dis)
print(count)