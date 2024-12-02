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
while i <= (len(a)-1):
    r += abs(a[i]-b[i])
    i += 1

print(r)