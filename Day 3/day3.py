import re

mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"
do_regex = r"do\(\)"
dont_regex = r"don't\(\)"

result = 0
with open("Day 3/input/input.txt") as f:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", f.read())

do = True
result = result2 = 0 
for match in matches:
    if re.fullmatch(mul_regex,match):
        mul = re.findall(mul_regex,match)[0]
        result += int(mul[0]) * int(mul[1])
    if re.fullmatch(mul_regex,match) and do:
        mul = re.findall(mul_regex,match)[0]
        result2 += int(mul[0]) * int(mul[1])
    if re.fullmatch(do_regex,match):
        do = True
    if re.fullmatch(dont_regex,match): 
        do = False

print("Part1:", result)
print("Part2:", result2)

