'''
trailhead is every 0 in map
ends is every 9
trailhead rating is how many different possible paths that trailhead has
find sum of all trailhead ratings
'''
def find_score(coord1,coord2,currentnum=0):
    global score
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
        match = find_score((checkleft,y),coord2,currentnum+1)
        if match:
            score +=1
    # right
    if (checkright < len(map)) and (int(map[y][checkright]) == currentnum+1):
        match = find_score((checkright,y),coord2,currentnum+1)
        if match:
            score += 1
    # up
    if (checkup > -1) and (int(map[checkup][x]) == currentnum+1):
        match = find_score((x,checkup),coord2,currentnum+1)
        if match:
            score +=1 
    # down
    if (checkdown < len(map)) and (int(map[checkdown][x]) == currentnum+1):
        match = find_score((x,checkdown),coord2,currentnum+1)
        if match:
            score +=1


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
# compare every trailhead to every end, adds score to count
for trailhead in trailheads:
    for end in ends:
        score = 0
        find_score(trailhead,end)
        count += score

print(count)