p = [[' '] * 50 for _ in range(30)]


def yield_decoration(interval):
    count = 0
    while True:
        yield 'O' if count % interval == 0 else '*'
        count += 1


def tree(h: int, v: int, l: int = 0, c: int = 0):  # height
    deco = yield_decoration(v)
    l, c = l, c  # top of tree (not star), and center of tree; no offsets... trial and error.
    p[l][c] = 'X'
    p[l + 1][c] = '^'

    for i in range(h-1):
        p[l+i+2][c-i-1] = '/'

        for d in range(i * 2 + 1):
            p[l+i+2][c-i+d] = next(deco) if d % 2 == 1 else '*'

        # p[l+i+2][c-i+i*2+1] = '\\'
        p[l+i+2][c+i+1] = '\\'

    p[l+h+1][c-1], p[l+h+1][c+1] = '|', '|'


def tree_old(h: int, v: int):  # height
    deco = yield_decoration(v)
    c = h-1  # center
    print(' ' * c, end='')
    print('X')
    print(' ' * c, end='')
    print('^')

    for i in range(h-1):
        print(' ' * (c-i-1), end='')
        print('/', end='')

        line = ''.join([next(deco) if d % 2 == 1 else '*' for d in range((i * 2 + 1))])
        print(line, end='')

        print('\\', end='')
        print()

    print(' ' * (c-1), end='')
    print('| |')


# tree(4, 2, 10, 20)
# line = list(map(int, "4 2 10 20 10 4 9 25".split()))
# line = list(map(int, "7 3 7 37".split()))
# line = list(map(int, "4 2 0 0".split()))
line = list(map(int, input().split()))

if len(line) == 2:
    tree_old(line[0], line[1])
else:
    # making boarders
    for i in range(30):
        p[i][0], p[i][-1] = '|', '|'

    for i in range(50):
        p[0][i], p[-1][i] = '-', '-'

    for i, c in enumerate(list('Merry Xmas')):
        p[27][20 + i] = c

    args = list(zip(line[::4], line[1::4], line[2::4], line[3::4]))

    for h, i, l, c in args:
        tree(h, i, l, c)

    for r in p:
        for c in r:
            print(c, end='')
        print()
