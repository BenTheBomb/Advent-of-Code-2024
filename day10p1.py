'''
trailhead is every 0
ends is every 9
trailhead score is how many ends are reachable from trailhead
find sum of all trailhead scores
'''
# Return boolean of whether the first coord can reach the second
# coords are tuples (x,y)
def can_reach(coord1,coord2,currentnum=0):
    if currentnum == 9:
        return coord1 == coord2

    x = coord1[0]
    y = coord1[1]
    checkleft = x-1
    checkright = x+1
    checkup = y-1
    checkdown = y+1

    # left
    if (checkleft > -1) and (int(map[y][checkleft]) == currentnum+1):
        match = can_reach((checkleft,y),coord2,currentnum+1)
        if match:
            return True
    # right
    if (checkright < len(map)) and (int(map[y][checkright]) == currentnum+1):
        match = can_reach((checkright,y),coord2,currentnum+1)
        if match:
            return True
    # up
    if (checkup > -1) and (int(map[checkup][x]) == currentnum+1):
        match = can_reach((x,checkup),coord2,currentnum+1)
        if match:
            return True
    # down
    if (checkdown < len(map)) and (int(map[checkdown][x]) == currentnum+1):
        match = can_reach((x,checkdown),coord2,currentnum+1)
        if match:
            return True
    return False
    

with open('day10.txt','r') as f:
    map = f.read().split()

# saves coords of every 0 as (x,y)
trailheads = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '0':
            trailheads.append((j,i))

# saves coords of every 9
ends = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '9':
            ends.append((j,i))

count = 0
# compare every trailhead to every end, if it can reach, add 1 to count
for trailhead in trailheads:
    for end in ends:
        if can_reach(trailhead,end) == True:
            count += 1

print(count)