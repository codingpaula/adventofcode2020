with open('9.txt') as file:
    entries = [int(entry.strip()) for entry in file]


def createPreambleSums(preamble: list):
    i = 0
    sums = []
    while i < len(preamble):
        j = i + 1
        while j < len(preamble):
            sums.append(preamble[i] + preamble[j])
            j = j + 1
        i = i + 1
    return sums


preamble = []
index = 25
foundFirst = False
brokenNumber = 0
while index < len(entries) and not foundFirst:
    preamble = entries[index-25:index]
    questioned = entries[index]
    possibleSums = createPreambleSums(preamble)
    if not questioned in possibleSums:
        foundFirst = True
        brokenNumber = questioned
        print('nope', entries[index], index)
    index = index + 1


startingAt = 0
sumTil = 1
foundSet = False
while not foundSet:
    while sumTil < len(entries) and not foundSet:
        possibleSum = sum(entries[startingAt:sumTil+1])
        if possibleSum == brokenNumber:
            correctSet = entries[startingAt:sumTil+1]
            correctSet.sort()
            print(correctSet[0] + correctSet[len(correctSet)-1])
            foundSet = True
        sumTil = sumTil + 1
    startingAt = startingAt + 1
    sumTil = startingAt + 1
print(questioned)
