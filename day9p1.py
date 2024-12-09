'''
every other value is length of block, then length of space
three steps:
write line with '.' as empty space
sort numbers until all empty space is gone
compute sum
'''
with open('day9.txt','r') as f:
    step0 = f.read()

withspace = []

for i in range(len(step0)):
    if i % 2 == 0:
        for j in range(int(step0[i])):
            withspace.append(i//2)
    elif i%2 == 1:
        for j in range(int(step0[i])):
            withspace.append('.')

withoutspace = withspace.copy()

while '.' in withoutspace:
    firstspace = withoutspace.index('.')
    lastvalue = withoutspace.pop()
    withoutspace[firstspace] = lastvalue
    while withoutspace[-1] == '.':
        withoutspace.pop()

sum = 0
for i in range(len(withoutspace)):
    sum += i * withoutspace[i]

print(sum)