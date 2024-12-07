'''
coordinate system for map
    list w/ nested lists as rows & columns

find '^' as starting position
keep track of current position and direction

while current position is within bounds:
    check in front of current position
    if '#' in the way:
        upate direction (turn right)
    if '#' not in the way:
        replace current position with 'X'
        update position (go forward 1)

count total 'X's
'''
with open('day6.txt', 'r') as f:
    content = f.read()
map = content.split()

xpos = 0
ypos = 0
dir = '^'

# find start position
for i in range(len(map)):
    if '^' in map[i]:
        ypos = i
        xpos = map[i].find('^')
        break

xbound = 129
ybound = 129
        
while (xpos > -1) and (xpos < xbound) and (ypos > -1) and (ypos < ybound):
    print(xpos,ypos)
    print(dir)
    if dir == '^':
        if map[ypos-1][xpos] == '#':
            # rotate if in front of '#'
            dir = '>'
        else:
            # rewrite current position as 'X'
            map[ypos] = map[ypos][:xpos] + 'X' + map[ypos][xpos+1:]
            # change current position
            ypos -= 1
    elif dir == '>':
        if map[ypos][xpos+1] == '#':
            dir = 'v'
        else:
            map[ypos] = map[ypos][:xpos] + 'X' + map[ypos][xpos+1:]
            xpos += 1
    elif dir == 'v':
        if map[ypos+1][xpos] == '#':
            dir = '<'
        else:
            map[ypos] = map[ypos][:xpos] + 'X' + map[ypos][xpos+1:]
            ypos += 1
    elif dir == '<':
        if map[ypos][xpos-1] == '#':
            dir = '^'
        else:
            map[ypos] = map[ypos][:xpos] + 'X' + map[ypos][xpos+1:]
            xpos -= 1

# edge case
if map[ypos][xpos] == '.':
    map[ypos] = map[ypos][:xpos] + 'X' + map[ypos][xpos+1:]

# count 'X's
sum = 0
for line in map:
    sum += line.count('X')

print(sum)

