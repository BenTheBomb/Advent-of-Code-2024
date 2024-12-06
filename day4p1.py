'''
put each line as value in array
running total of count
check each line
    find 'xmas' and 'samx'
check each column
check positive diagonal
check negative diagonal

'''

with open("day4.txt", "r") as f:
    content = f.read()

lines = content.split()
count = 0

# check each line
for line in lines:
    count += line.count("XMAS")
    count += line.count("SAMX")

# check each column
columns = [''] * len(lines)
for i in range(len(lines)):
    for j in range(len(lines)):
        columns[i] += lines[j][i]

for column in columns:
    count += column.count("XMAS")
    count += column.count("SAMX")

# diagonals
posdiagonal = [''] * (2 * len(lines) - 1)

for i in range(len(lines)):
    x = i
    for j in range(len(lines)):
        posdiagonal[x] += lines[i][j]
        x += 1

for diagonal in posdiagonal:
    count += diagonal.count("XMAS")
    count += diagonal.count("SAMX")


negdiagonal = [''] * len(posdiagonal)

for i in range(len(lines)):
    x = i
    for j in range(len(lines)-1,-1,-1):
        negdiagonal[x] += lines[i][j]
        x += 1

for diagonal in negdiagonal:
    count += diagonal.count("XMAS")
    count += diagonal.count("SAMX")

print(count)