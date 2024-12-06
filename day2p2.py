'''
isolate each report (each line)
put levels(each value) as value in array
each array will have len(array) additional similar arrays, with one missing number each
if any single additional array is safe, then add 1 to count

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

def safe_check(array):
    subArray = []
    for i in range(len(array) - 1):
        subArray.append(array[i+1] - array[i])

    r1start, r1end = 1, 3
    r2start, r2end = -3, -1

    return all(r1start <= num <= r1end for num in subArray) or all(r2start <= num <= r2end for num in subArray)

with open("day2.txt","r") as f:
    for line in f:
        strArray = line.split()
        intArray = [int(x) for x in strArray]
        expandArray = []
        expandArray.append(intArray)
    
        for i in range(len(intArray)):
            newIntArray = intArray.copy()
            newIntArray.pop(i)     
            expandArray.append(newIntArray)

        subcount = 0
        for array in expandArray:
            subcount += safe_check(array)
        if subcount > 0:
            count += 1
print(count)