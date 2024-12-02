a = []
b = []

with open("Day 1\input\input") as f:
    for line in f:
        x, y = line.strip().split("   ")
        a.append(int(x))
        b.append(int(y))

a.sort()
b.sort()

r = i = 0
for i in a:
    r += i*b.count(i)
print(r)