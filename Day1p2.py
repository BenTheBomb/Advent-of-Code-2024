array1 = []
array2 = []

with open("day1.txt", "r") as f:
    for line in f:
        strArray = line.split()
        array1.append(int(strArray[0]))
        array2.append(int(strArray[1]))

score = 0
for value in array1:
    factor = array2.count(value)
    score += value * factor

print(score)