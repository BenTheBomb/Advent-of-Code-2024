'''
very similar to p1

instead of creating two antinodes, create as many as possible within bounds
find highest possible position for antinode
while antinode is within bounds:
    add '#' to antinodemap
    go to next possible position
'''
# inputs character, outputs number of that character in map
def count_occurence(character):
    tally = 0
    for i in range(ybound):
        tally += map[i].count(character)
    return tally

# inputs character and previous occurence number, outputs coords of next occurence
def find_occurence(character,previous):
    count = 0
    for y in range(ybound):
        xindex = map[y].find(character)
        if xindex == -1:
            continue
        count += 1
        if count <= previous:
            continue
        return (xindex, y)

def replace_char_in_str(string,character,index):
    return string[:index] + character + string[index+1:]

with open('day8.txt', 'r') as f:
    content = f.read()
map = content.split()
antinodemap = map.copy()

xbound = len(map[0])
ybound = len(map)

string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in string:
    occurences = count_occurence(char)
    for i in range(occurences-1):
        first = find_occurence(char,i)
        for j in range(occurences-i-1):
            second = find_occurence(char,j+i+1)
            difference = (second[0]-first[0],second[1]-first[1])
            startantinode = first + tuple()
            # find starting position
            while (-1 < startantinode[0] < xbound) and (-1 < startantinode[1] < ybound):
                startantinode = (startantinode[0]-difference[0],startantinode[1]-difference[1])
            # test possible positions for antinode, write '#' if within bounds
            antinode = (startantinode[0]+difference[0],startantinode[1]+difference[1])
            while (-1 < antinode[0] < xbound) and (-1 < antinode[1] < ybound):
                antinodemap[antinode[1]] = replace_char_in_str(antinodemap[antinode[1]],'#',antinode[0])
                antinode = (antinode[0]+difference[0],antinode[1]+difference[1])

sum = 0
for line in antinodemap:
    sum += line.count('#')
print(sum)