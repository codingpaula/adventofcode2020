import math

with open('5.txt') as file:
    entries = [entry.strip() for entry in file]


def calculateSeatId(row: int, column: int):
    return row * 8 + column


def findNewRange(min: int, max: int, index: int, values: str):
    if min == max or index == len(values):
        return min
    if values[index] == 'F' or values[index] == 'L':
        middle = math.floor((max - min) / 2) + min
        return findNewRange(min, middle, index+1, values)
    if values[index] == 'B' or values[index] == 'R':
        middle = math.ceil((max - min) / 2) + min
        return findNewRange(middle, max, index+1, values)


seats = []
highestseat = 0
lowestseat = 800
for entry in entries:
    row = findNewRange(0, 127, 0, entry[0:7])
    column = findNewRange(0, 7, 0, entry[7:])
    seatId = row * 8 + column
    if seatId == 0:
        print(entry)
    seats.append(seatId)
    if seatId > highestseat:
        highestseat = seatId
    if seatId < lowestseat:
        lowestseat = seatId


seats.sort()
index = 1
while index < len(seats):
    if seats[index-1] < seats[index]-1:
        print('your seat: ', seats[index]-1)
    index = index + 1

print('lowest seat: ', lowestseat)
print('highest seat: ', highestseat)
