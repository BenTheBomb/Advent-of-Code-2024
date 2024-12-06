'''
search for string + integer combo "mul("#","#")"
multiply the two integers inside
add result to sum

'''
import re

sum = 0

with open("day3.txt","r") as f:
    content = f.read()
parsed = re.findall(r"mul\(\d+,\d+\)",content)

for item in parsed:
    stringint = re.findall(r"\d+",item)
    array = []
    for value in stringint:
        array.append(int(value))
    sum = sum + array[0] * array[1]
print(sum)
