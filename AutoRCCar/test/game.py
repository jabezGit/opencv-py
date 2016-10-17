pos = [0 for x in range(7)]
for i in range(3):
    pos[i] = -1
for i in range(3):
    pos[6 - i] = 1
# print(pos)
repos = pos[::-1]
count = 0


def kltry():
    global count, pos, repos

    if pos == repos:
        print('OK')
        exit()
    blank = pos.index(0)
    if blank >= 1 and pos[blank - 1] < 0:
        pos[blank] = -1
        pos[blank - 1] = 0
        print(str(blank - 1) + '->' + str(blank))
        kltry()
        pos[blank] = 0
        pos[blank - 1] = -1
        print('return')

    if blank >= 2 and pos[blank - 2] < 0:
        pos[blank] = -1
        pos[blank - 2] = 0
        print(str(blank - 2) + '->' + str(blank))
        kltry()
        pos[blank] = 0
        pos[blank - 2] = -1
        print('return')

    if blank <= 5 and pos[blank + 1] > 0:
        pos[blank] = 1
        pos[blank + 1] = 0
        print(str(blank) + '<-' + str(blank + 1))
        kltry()
        pos[blank] = 0
        pos[blank + 1] = 1
        print('return')

    if blank <= 4 and pos[blank + 2] > 0:
        pos[blank] = 1
        pos[blank + 2] = 0
        print(str(blank) + '<-' + str(blank + 2))
        kltry()
        pos[blank] = 0
        pos[blank + 2] = 1
        print('return')


kltry()