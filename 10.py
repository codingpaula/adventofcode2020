with open('10.txt') as file:
    entries = [int(entry.strip()) for entry in file]

entries.sort()
entries = entries + [entries[len(entries)-1] + 3]

currentJolt = 0
index = 0
ones = 0
twos = 0
threes = 0

while currentJolt <= entries[len(entries)-1] + 3 and index < len(entries):
    if currentJolt - entries[index] == -1:
        ones = ones + 1
    elif currentJolt - entries[index] == -2:
        twos = twos + 1
    elif currentJolt - entries[index] == -3:
        threes = threes + 1
    currentJolt = entries[index]
    index = index + 1

print('1-differences * 3-differences', ones * threes)

possibilities = dict.fromkeys([0] + entries, [])


def allPossibleNexts(array: list, current: int):
    i = 0
    while i < len(array):
        if array[i] - current > 3:
            return array[0:i]
        i = i + 1
    return array


index = 0
for poss in possibilities:
    possibilities[poss] = allPossibleNexts(entries[index:index+3], poss)
    index = index + 1

solutions = []


def nextAdapter(path: list, current: int, highest: int):
    if current == highest:
        solutions.append(path + [current])
    elif current < highest:
        [nextAdapter(path + [current], c, highest)
         for c in possibilities[current]]
    else:
        print(path + [current])


# calculate which adapters are necessary
mustHaves = []
for poss in possibilities:
    if len(possibilities[poss]) == 1 and possibilities[poss][0] - poss == 3:
        mustHaves.append(poss)


startPoint = 0
countSolutions = []
for must in mustHaves:
    solutions = []
    nextAdapter([], startPoint, must)
    countSolutions.append(len(solutions))
    startPoint = possibilities[must][0]


def product(numbers: list):
    product = 1
    for num in numbers:
        product = product * num
    return product


print('necessary adapter values:', mustHaves)
print('possible variations:', product(countSolutions))
