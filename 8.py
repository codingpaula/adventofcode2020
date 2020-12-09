with open('8.txt') as file:
    entries = [entry.strip().split(' ') for entry in file]


def checkIfCrashes(entries: list):
    pointer = 0
    crash = False
    success = False
    acc = 0

    alreadyCalled = dict()
    index = 0
    while index < len(entries):
        alreadyCalled.update({index: 0})
        index = index + 1

    while not crash and pointer < len(alreadyCalled) and not success:
        if alreadyCalled[pointer] > 0:
            crash = True
        else:
            alreadyCalled[pointer] = 1
            if entries[pointer][0] == 'acc':
                acc = acc + int(entries[pointer][1])
                pointer = pointer + 1
            elif entries[pointer][0] == 'nop':
                pointer = pointer + 1
            elif entries[pointer][0] == 'jmp':
                pointer = pointer + int(entries[pointer][1])
                if pointer == len(alreadyCalled):
                    success = True

    return (pointer, alreadyCalled, acc, crash, success)


changedAt = 0
runsThrough = False
accumulator = 0
while changedAt < len(entries) and runsThrough is False:
    if entries[changedAt][0] != 'acc':
        changedEntries = entries[0:changedAt] + [['jmp' if entries[changedAt][0]
                                                  == 'nop' else 'nop', entries[changedAt][1]]] + entries[changedAt+1:]
        result = checkIfCrashes(changedEntries)
        runsThrough = not result[3]
        accumulator = result[2]
        print(changedAt, result[0], result[2], result[3], result[4])
    changedAt = changedAt + 1


result = checkIfCrashes(entries)
print(result[3])
print(result[0])
print(entries[result[0]])
print(result[2])
print(accumulator)
print(changedAt)
