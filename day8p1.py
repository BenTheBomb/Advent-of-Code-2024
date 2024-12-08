'''
two maps: original input, and antinode map
coordinates
bounds

for each character (0-9, a-z, A-Z):
    count number of occurences in map
    keep track of which occurence its on
    if occurence number = number of occurences
        go to next character
    find first occurence in map
    find next occurence in map
    get coordinate difference betwen the two
    first antinode will be first occurence - coordinate difference
    second antinode will be second occurence + coordinate difference
    check if antinodes are within bounds, write '#' to antinode map

read number of '#'s in antinode map
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
            antinode1 = (first[0]-difference[0],first[1]-difference[1])
            antinode2 = (second[0]+difference[0],second[1]+difference[1])
            
            # if antinode is within bounds, write '#' to antinode map
            if (-1 < antinode1[0] < xbound) and (-1 < antinode1[1] < ybound):
                antinodemap[antinode1[1]] = replace_char_in_str(antinodemap[antinode1[1]],'#',antinode1[0])
            if (-1 < antinode2[0] < xbound) and (-1 < antinode2[1] < ybound):
                antinodemap[antinode2[1]] = replace_char_in_str(antinodemap[antinode2[1]],'#',antinode2[0])

sum = 0
for line in antinodemap:
    sum += line.count('#')
print(sum)