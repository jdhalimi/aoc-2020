import re

INPUT = '02.txt'
PATTERN = re.compile('(\d+)-(\d+) (\w): (\w+)')


def get_data():
    lines = []
    with open(INPUT) as f:
        for x in f:
            a, b, c, p = PATTERN.match(x).groups()
            a, b = int(a), int(b)
            lines.append((a, b, c, p))
    return lines


def day_02_01():
    data = get_data()
    valid_passwords = [p for a, b, c, p in data if a <= p.count(c) <= b]
    return len(valid_passwords)


def day_02_02():
    data = get_data()
    valid_passwords = [p for a, b, c, p in data if int(p[a - 1] == c) + int(p[b - 1] == c) == 1]
    return len(valid_passwords)


def test_get_data():
    for a, b, c, p in get_data():
        assert a < b


def test_day_02_01():
    assert day_02_01() == 456


def test_day_02_02():
    assert day_02_02() == 308
