with open('1.txt') as file:
    entries = [int(entry.strip()) for entry in file]


def findTwoEntries():
    smaller = []
    larger = []

    for num in entries:
        if num < 1010:
            smaller.append(num)
        else:
            larger.append(num)

    smaller.sort()
    larger.sort(reverse=True)

    for small in smaller:
        for large in larger:
            if small + large == 2020:
                print(small, large, small*large)
                return small * large


def findThreeEntries():
    smaller = []
    middle = []
    larger = []
    for num in entries:
        if num < 674:
            smaller.append(num)
        if num < 1347:
            middle.append(num)
        else:
            larger.append(num)

    for one in smaller:
        for two in middle + larger:
            num = one + two
            if num <= 1346:
                for three in middle:
                    if one + two + three == 2020:
                        return one*two*three
            if num < 2020:
                for three in smaller:
                    if one + two + three == 2020:
                        return one*two*three


result = findTwoEntries()
print(result)
threes = findThreeEntries()
print(threes)
