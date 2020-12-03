with open('3.txt') as file:
    map = [entry.strip() for entry in file]


def testSlopes(right: int, down: int):
    position = (0, 0)
    trees = 0
    while position[1] < len(map):
        row = map[position[1]]
        if row[position[0] % len(row)] == '#':
            trees = trees + 1
        position = (position[0]+right, position[1]+down)
    return trees


testCases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
result = 1

for case in testCases:
    ergebnis = testSlopes(case[0], case[1])
    results.append(ergebnis)
    result = result * ergebnis

print(results)
print(result)
