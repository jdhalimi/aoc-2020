INPUT = '03.txt'


def get_data():
    with open(INPUT) as f:
        numbers = [x.strip() for x in f]
    return numbers


def day_03_01(x, y):
    data = get_data()
    n = 0
    line = data.pop(0)
    s = len(line)
    i = 0
    while data:
        for _ in range(y):
            line = data.pop(0)
        i = (i + x) % s
        if line[i] == '#':
            n += 1
    return n


def day_03_02():
    m = 1
    for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        m *= day_03_01(x, y)
    return m


def test_day_03_01():
    assert day_03_01(3, 1) == 282


def test_day_03_02():
    assert day_03_02() == 282
