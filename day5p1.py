'''
two different lists, both with nested lists
    first has lists of ordering rules
    second has lists of page numbers

function to check page numbers to rules
    compare indices, not values (can keep rules as strings??)

if page numbers follow rules, add to new list
if not, discard
iterate through every list

to find middle page number of each list
    index is (len(list)-1)/2
add middle number to running sum
'''
def check(page):
    valid = True
    for i in range(len(page)):
        for j in range(len(rules)):
            rule = rules[j]
            if rule[0] in page[i]:
                for k in range(len(page)):
                    if (not (rule[1] in page[k])) or (k == i):
                        continue
                    elif page.index(rule[0]) < page.index(rule[1]):
                        continue
                    elif page.index(rule[0]) > page.index(rule[1]):
                        valid = False
                        break
        if valid == False:
            break
    if valid:
        correct.append(page)
    else:
        return 0


with open('day5.txt','r') as f:
    content = f.read()

rules = content.split('\n\n')[0].split()
pages = content.split('\n\n')[1].split()

for i in range(len(rules)):
    rules[i] = rules[i].split('|')

for i in range(len(pages)):
    pages[i] = pages[i].split(',')


correct = []
for page in pages:
    check(page)

sum = 0
for item in correct:
    center = (len(item)-1)//2
    sum += int(item[center])

print(sum)