'''
same coordinate system as p1
start position is same
bounds are same

list of unique coordinates from entire path
for each unique coordinate (except starting position), test adding an obstacle there

function for test
same path algorithm as p1, plus collecting unique (positions and direction)
if new combined position and direction match, its a looped path
    add one to running tally
if path reaches edge, not a looped path
    go to next path
'''

# compares to uniques: if new, add to set. if not, discard
# input is a tuple (# xcoord, # y coord) or (# xcoord, # y coord, # direction)
# output is boolean
def compare_coords(coords):
    isunique = True
    if len(coords) == 2:
        if coords in uniquecoords:
            isunique = False
        uniquecoords.add(coords)
    elif len(coords) == 3:
        if coords in uniquecoordsdir:
            isunique = False
        uniquecoordsdir.add(coords)
    return isunique

# checks if adding obstacle at (coords) creates a repeating loop
def testobstacle(coords):
    submap = map.copy()
    # adds the obstacle
    submap[coords[1]] = submap[coords[1]][:coords[0]] + '#' + submap[coords[1]][coords[0]+1:]
    loop = False
    xpos = startxpos
    ypos = startypos
    dir = 1
    # starts path process
    while (xpos > -1) and (xpos < xbound) and (ypos > -1) and (ypos < ybound):
        if dir == 1:
            if submap[ypos-1][xpos] == '#':
                # if both coordinates and direction have been used before, it is a loop
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                # rotate if in front of '#'
                dir = 2
            else:
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                # change current position
                ypos -= 1
        elif dir == 2:
            if submap[ypos][xpos+1] == '#':
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                dir = 3
            else:
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                xpos += 1
        elif dir == 3:
            if submap[ypos+1][xpos] == '#':
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                dir = 4
            else:
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                ypos += 1
        elif dir == 4:
            if submap[ypos][xpos-1] == '#':
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                dir = 1
            else:
                if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop
                xpos -= 1
    if not compare_coords((xpos,ypos,dir)):
                    loop = True
                    return loop


with open('day6.txt', 'r') as f:
    content = f.read()
map = content.split()

startxpos = 0
startypos = 0
dir = 1

# find start position
for i in range(len(map)):
    if '^' in map[i]:
        startypos = i
        startxpos = map[i].find('^')
        break

xpos = startxpos
ypos = startypos

xbound = len(map[ypos])-1
ybound = len(map)-1

# unique coordinate for original path
uniquecoords = set()

# original path
while (xpos > -1) and (xpos < xbound) and (ypos > -1) and (ypos < ybound):
    if dir == 1:
        if map[ypos-1][xpos] == '#':
            # rotate if in front of '#'
            dir = 2
        else:
            compare_coords((xpos,ypos))
            # change current position
            ypos -= 1
    elif dir == 2:
        if map[ypos][xpos+1] == '#':
            dir = 3
        else:
            compare_coords((xpos,ypos))
            xpos += 1
    elif dir == 3:
        if map[ypos+1][xpos] == '#':
            dir = 4
        else:
            compare_coords((xpos,ypos))
            ypos += 1
    elif dir == 4:
        if map[ypos][xpos-1] == '#':
            dir = 1
        else:
            compare_coords((xpos,ypos))
            xpos -= 1

# edge case
compare_coords((xpos,ypos))

sum = 0
for item in uniquecoords:
    # skips start position because it is occupied by guard
    if item == (startxpos,startypos):
        continue
    
    uniquecoordsdir = set()
    if testobstacle(item):
        sum += 1

print(sum)