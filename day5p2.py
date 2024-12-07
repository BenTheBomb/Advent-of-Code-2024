'''
check function same as p1, but saves incorrect pages

function to sort incorrect pages
recursive??

adding middle numbers same as p1
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
    return valid

def sort(page):
    for i in range(len(page)):
        for j in range(len(rules)):
            rule = rules[j]
            if rule[0] in page[i]:
                for k in range(1,len(page)-1):
                    if (k+i < len(page)) and (rule[1] in page[k+i]):
                        if page.index(rule[0]) < page.index(rule[1]):
                            continue
                        elif page.index(rule[0]) > page.index(rule[1]):
                            page[page.index(rule[0])], page[page.index(rule[1])] = page[page.index(rule[1])], page[page.index(rule[0])]
                            sort(page)
            elif rule[1] in page[i]:
                for k in range(1,len(page)-1):
                    if (k+i < len(page)) and (rule[0] in page[k+i]):
                        if page.index(rule[0]) < page.index(rule[1]):
                            continue
                        elif page.index(rule[0]) > page.index(rule[1]):
                            page[page.index(rule[0])], page[page.index(rule[1])] = page[page.index(rule[1])], page[page.index(rule[0])]
                            sort(page)
    return(page)

with open('day5.txt','r') as f:
    content = f.read()

rules = content.split('\n\n')[0].split()
pageslist = content.split('\n\n')[1].split()

for i in range(len(rules)):
    rules[i] = rules[i].split('|')

for i in range(len(pageslist)):
    pageslist[i] = pageslist[i].split(',')


correct = []
incorrect = []
for pages in pageslist:
    if check(pages):
        correct.append(pages)
    else:
        incorrect.append(pages)

fixed = []
for item in incorrect:
    fixed.append(sort(item))

sum = 0
for item in fixed:
    center = (len(item)-1)//2
    sum += int(item[center])

print(sum)