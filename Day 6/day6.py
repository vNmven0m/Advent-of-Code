def move_guard(guard_pos, obstacles, direction):
    x, y = guard_pos
    # Directions: 0 = up, 1 = right, 2 = down, 3 = left
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = deltas[direction]
    new_pos = (x + dx, y + dy)
    
    if new_pos not in obstacles:
        return new_pos, direction, 1 
    else:
        return guard_pos, (direction + 1) % 4, 0

with open("Day 6/input/input.txt") as f:
    obstacles = set()
    visited = set()    
    row = 0
    direction = 0
    guard_pos = None
    
    for line in f:
        col = 0
        for c in line.strip():
            if c == "#":
                obstacles.add((row, col))
            elif c == "^":
                guard_pos = (row, col)
            col += 1
        row += 1

result = 0
visited.add(guard_pos)

row, col

while 0 <= guard_pos[0] < row and 0 <= guard_pos[1] < col:
    guard_pos, direction, move = move_guard(guard_pos, obstacles, direction)
    if guard_pos not in visited:
        visited.add(guard_pos)
        result += move

print(result)
