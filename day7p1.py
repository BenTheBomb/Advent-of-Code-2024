'''
function to compare each test value to all combinations of left values
interpret string operator as an operation

sum of result values that are possible
'''
# if the result isn't possible, outputs False
# if the result is possible, outputs result
def checkvalue(result, values):
    while len(values) > 1:
        sum = values[0] + values[1]
        sumvalues = values[1:]
        sumvalues[0] = sum
        match = checkvalue(result,sumvalues)
        if match:
            return True
        else: 
            mult = values[0] * values[1]
            multvalues = values[1:]
            multvalues[0] = mult
            return checkvalue(result, multvalues)
    else:
        return values[0] == result


with open('day7.txt','r') as f:
    content = f.read().split('\n')

testresults = []
strtestvalues = []

for line in content:
    testresults.append(int(line[:line.index(':')]))
    strtestvalues.append(line[line.index(': ')+2:])
    
testvalues = []
for value in strtestvalues:
    value = value.split()
    testvalues.append([int(x) for x in value])

count = 0
for i in range(len(testresults)):
    if checkvalue(testresults[i],testvalues[i]):
        count += testresults[i]
print(count)



