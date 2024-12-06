'''
get every 3x3 from input
function to check if 3x3 contains x-mas
running total

options for x-mas:
mmass
msams
ssamm
smasm
'''

def xmas(str):
    abvstr = str[0:9:2]
    
    if (abvstr=='MMASS') or (abvstr=='MSAMS') or (abvstr=='SSAMM') or (abvstr=='SMASM'):
        return 1
    else:
        return 0


with open("day4.txt", "r") as f:
    content = f.read()
lines = content.split()

threes = []
for i in range(len(lines)-2):
    for j in range(len(lines)-2):
        threes.append(lines[i][j:j+3]+lines[i+1][j:j+3]+lines[i+2][j:j+3])

count = 0
for string in threes:
    count += xmas(string)

print(count)