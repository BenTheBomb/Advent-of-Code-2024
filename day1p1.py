array1 = []
array2 = []

with open("day1.txt", "r") as f:
    for line in f:
        strArray = line.split()
        array1.append(int(strArray[0]))
        array2.append(int(strArray[1]))

array1.sort()
array2.sort()

count = 0
for i in range(len(array1)):
    count += abs(array1[i] - array2[i])

print(count)

