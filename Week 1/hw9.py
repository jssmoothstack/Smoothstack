#1+2

accounting = [[34587, "Learning Python, Mark Lutz", 4, 40.95],
[98762, "Programming Python, Mark Lutz", 5, 56.80],
[77226, "Head First Python, Paul Barry", 3, 32.95],
[88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

def routine(info):
    return (info[0], info[2]*info[3]) if info[2]*info[3] >= 100 else (info[0], info[2]*info[3] + 10)

print(list(map(routine, accounting)))

#3

accounting2 = [[34587, (1, 4, 40.95)],
[98762, (2, 5, 56.80)],
[77226, (3, 3, 32.95)],
[88112, (4, 3, 24.99)]]

def routine2(info):
    return (info[0], info[1][1]*info[1][2])

print(list(map(routine2, accounting2)))