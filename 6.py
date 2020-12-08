with open('6.txt') as file:
    entries = [entry.strip() for entry in file]


answers = []
group = []
counts = []
for entry in entries:
    if entry != '':
        group.append(entry)
    else:
        answers.append(group)
        group = []


part1 = []
part2 = []
groups = []
count2 = 0
for g in answers:
    string = ''
    for element in g:
        string = string + element
    allAnswersInGroup = sorted(string)
    duplicates = dict.fromkeys(allAnswersInGroup, 0)
    for element in allAnswersInGroup:
        duplicates[element] = duplicates[element] + 1
    singles = list(dict.fromkeys(allAnswersInGroup))
    part1.append(singles)
    part2.append(duplicates)
    groups.append(len(g))
    counts.append(len(singles))
    for element in duplicates:
        if duplicates[element] == len(g):
            count2 = count2 + 1


print(groups[0:10])
print(sum(counts))
print(count2)
