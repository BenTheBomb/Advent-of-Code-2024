'''
isolate each report (each line)
put levels(each value) as value in array

check for unsafeness
    subtract each value from adjacent
    increasing/decreasing check
        values must be all negative or all positive (no 0)
    gradual change check
        must be between -1 & -3 or 1 and 3

if unsafe, skip to next
if safe, add 1 to count, proceed to next
print count
'''
count = 0

def safe_check(line):
    strArray = line.split()
    intArray = [int(x) for x in strArray]
    subArray = []
    for i in range(len(intArray) - 1):
        subArray.append(intArray[i+1] - intArray[i])

    r1start, r1end = 1, 3
    r2start, r2end = -3, -1

    return all(r1start <= num <= r1end for num in subArray) or all(r2start <= num <= r2end for num in subArray)

with open("day2.txt","r") as f:
    for line in f:
        count += safe_check(line)

print(count)
