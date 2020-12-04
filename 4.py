import re

with open('4.txt') as file:
    entries = [entry.strip() for entry in file]

passports = []
contains = []

for entry in entries:
    if entry != '':
        for value in entry.split():
            contains.append(value)
    else:
        passports.append(contains)
        contains = []

valid = 0


def checkInBetween(field: int, min: int, max: int):
    if field >= min and field <= max:
        return True
    else:
        return False


def checkHeight(number: str, entity: str):
    if entity == 'cm':
        return checkInBetween(int(number), 150, 193)
    if entity == 'in':
        return checkInBetween(int(number), 59, 76)
    return False


def checkEyeColor(value: str):
    if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
        return True
    return False


def checkHairColor(color: str):
    if color[0] == '#' and len(color) == 7:
        if re.match(r'([0-9A-Fa-f]{6})', color[1:]) is not None:
            return True
    return False


def checkPid(pid: str):
    if len(pid) == 9 and re.match(r'([0-9]{9})', pid) is not None:
        return True
    return False


def whichProperty(field: str, value: str):
    if field == 'byr':
        return checkInBetween(int(value), 1920, 2002)
    if field == 'iyr':
        return checkInBetween(int(value), 2010, 2020)
    if field == 'eyr':
        return checkInBetween(int(value), 2020, 2030)
    if field == 'hgt':
        return checkHeight(value[0:len(value)-2], value[len(value)-2:len(value)])
    if field == 'hcl':
        return checkHairColor(value)
    if field == 'ecl':
        return checkEyeColor(value)
    if field == 'pid':
        return checkPid(value)
    if field == 'cid':
        return True
    return False


for passport in passports:
    if len(passport) >= 7:
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        passport = [value.split(':') for value in passport]
        for field in passport:
            validField = whichProperty(field[0], field[1])
            if validField:
                fields.remove(field[0])
        if fields == [] or fields == ['cid']:
            valid = valid + 1


print(valid)
