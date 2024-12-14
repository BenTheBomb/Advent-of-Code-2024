# checks if value is in list: if not, return false & add to list
def checkvalue(value):
    beenchecked = True
    if value in checkedvals:
        beenchecked = True
    elif not (value in checkedvals):
        beenchecked = False
        checkedvals.append(value)
    return beenchecked

with open('day9.txt','r') as f:
    step0 = f.read()

withspace = []

for i in range(len(step0)):
    if i % 2 == 0:
        withspace.append((str(i//2)*int(step0[i]),int(step0[i])))
    elif i%2 == 1:
        withspace.append('.'*int(step0[i]))

withoutspace = withspace.copy()
checkedvals = []

# both are indices (not the actual value)
currentvalue = len(withoutspace)-1
firstspace = 1

# goes through every value and finds a spot for it
while firstspace < currentvalue:
    # finds first open space in list
    for item in withoutspace:
        if type(item) == str:
            firstspace = withoutspace.index(item)
            break
    if firstspace > currentvalue:
        break

    currentspace = firstspace

    valuelength = withoutspace[currentvalue][1]
    spacelength = len(withoutspace[currentspace])

    foundspace = False
    for item in withoutspace[currentspace:currentvalue]:
        # if value is a string, and fits in the space
        if (type(item) == str) and (len(item) >= valuelength):
            currentspace = withoutspace.index(item)
            foundspace = True
            spacelength = len(withoutspace[currentspace])
            break

    # if value does fit
    if (spacelength >= valuelength) and (foundspace):
        leftoverspace = spacelength - valuelength
        takenspace = valuelength
        if leftoverspace > 0:
            withoutspace[currentspace] = '.'*takenspace
            withoutspace.insert(currentspace+1,'.'*leftoverspace)
            # swaps the values
            withoutspace[currentspace], withoutspace[currentvalue+1] = withoutspace[currentvalue+1], withoutspace[currentspace]
        else: 
            withoutspace[currentspace], withoutspace[currentvalue] = withoutspace[currentvalue], withoutspace[currentspace]

    # if the value is a tuple, and hasn't been checked yet, it becomes the current value
    while (type(withoutspace[currentvalue]) != tuple) or (checkvalue(withoutspace[currentvalue])):
        currentvalue -= 1

    # combines strings that are next to each other
    length = len(withoutspace)
    item = currentspace
    while (foundspace == True) and (item < length-1):
        if (type(withoutspace[item])==str) and (type(withoutspace[item+1])==str):
            if (item < length-2) and (type(withoutspace[item+2])==str):
                withoutspace[item] = withoutspace[item] + withoutspace[item+1]
                withoutspace.pop(item+1)
            withoutspace[item] = withoutspace[item] + withoutspace[item+1]
            withoutspace.pop(item+1)
        item += 1
        length = len(withoutspace)

separated = []

# puts each digit and empty space as own value in 'separated'
for item in withoutspace:
    if type(item) == tuple:
        digits = len(item[0]) // item[1]
        for i in range(item[1]):
            separated.append(int(item[0][0:digits]))
    else:
        for i in range(len(item)):
            separated.append('.')

# multiplys index # by value, adds to sum (ignores '.')
sum = 0
for i in range(len(separated)):
    if type(separated[i])==str:
        continue
    sum += i * separated[i]

print(sum)