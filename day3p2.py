'''
search for strings "do()" and "don't()"
split entire text up: keep start to first "don't()", 
 get rid of sections after "don't()" but before "do()", 
 keep sections after "do()" but befor "don't()
combine new sections into one

search for string + integer combo "mul("#","#")"
multiply the two integers inside
add result to sum
'''
import re

with open("day3.txt","r") as f:
    content = f.read()

fixed = ""
needsedit = content
include = True

while ("don't()" in needsedit) or ("do()" in needsedit):
    dontind = needsedit.find("don't()")
    doind = needsedit.find("do()")

    # checks for when there are no 'dont' or 'do'
    if (dontind == -1) and include:
        fixed += needsedit
        break
    elif (dontind == -1) and not include:
        fixed += needsedit[doind+4:]
        break
    elif (doind == -1) and include:
        fixed += needsedit[:dontind]
        needsedit = needsedit[dontind+7]
        continue
    elif (doind == -1) and not include:
        break
    
       
    if (dontind < doind) and include:
        # add the section to fixed, remove section + 'dont' from needsedit
        fixed += needsedit[:dontind]
        needsedit = needsedit[dontind+7:]
        include = False
    elif (doind < dontind) and include:
        # add section to fixed, remove section + 'do' from needsedit
        fixed += needsedit[:doind]
        needsedit = needsedit[doind+4:]
        include = True
    # remove smaller section from needsedit
    elif (dontind < doind) and (not include):
        needsedit = needsedit[dontind+7:]
        include = False
    elif (doind < dontind) and (not include):
        needsedit = needsedit[doind+4:]
        include = True


sum = 0
parsed = re.findall(r"mul\(\d+,\d+\)",fixed)

for item in parsed:
    stringint = re.findall(r"\d+",item)
    array = []
    for value in stringint:
        array.append(int(value))
    sum = sum + array[0] * array[1]

print(sum)
