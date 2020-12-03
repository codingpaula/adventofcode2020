with open('2.txt') as file:
    entries = [entry.strip().split() for entry in file]
    entries = [[entry[0].split('-'), entry[1][0], entry[2]]
               for entry in entries]


def sledPwdPolicy():
    count = 0
    for pwd in entries:
        contains = pwd[2].count(pwd[1])
        if contains >= int(pwd[0][0]) and contains <= int(pwd[0][1]):
            count = count+1
    return count


def tobogganPwdPolicy():
    count = 0
    for pwd in entries:
        first = pwd[2][int(pwd[0][0])-1]
        second = pwd[2][int(pwd[0][1])-1]
        if (first == pwd[1] and second != pwd[1]) or (first != pwd[1] and second == pwd[1]):
            count = count+1
    return count


sledPolicyCount = sledPwdPolicy()
tobogganPolicyCount = tobogganPwdPolicy()
print(sledPolicyCount)
print(tobogganPolicyCount)
