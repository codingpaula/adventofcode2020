with open('7.txt') as file:
    entries = [entry.strip() for entry in file]

rules = dict()
for entry in entries:
    words = entry.split(' ')
    bag = (words[0], words[1])
    bagsOrNo = words[4:]
    bags = []
    if bagsOrNo != ['no', 'other', 'bags.']:
        index = 0
        while index*4 < len(bagsOrNo):
            bags.append(
                [bagsOrNo[index*4], (bagsOrNo[index*4+1], bagsOrNo[index*4+2])])
            index = index + 1
    rules.update({bag: bags})


def contains(bag: tuple):
    if rules[bag] == []:
        return False
    for rule in rules[bag]:
        if rule[1] == ('shiny', 'gold'):
            return True
    else:
        containing = [contains(possible[1]) for possible in rules[bag]]
        for c in containing:
            if c:
                return True
        return False


run = []
count = 0
for rule in rules:
    if contains(rule):
        count = count + 1


def countBags(bag: tuple):
    if rules[bag] == []:
        return 1
    else:
        containing = [int(rule[0]) * countBags(rule[1]) for rule in rules[bag]]
        return 1 + sum(containing)


# do not count the shiny bag itself
shinyBags = countBags(('shiny', 'gold')) - 1
print(count)
print(shinyBags)
