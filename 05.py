INPUT = '05.txt'


def get_data():
    rows = []
    with open(INPUT) as f:
        for line in f:
            line = line.strip()
            rows.append(line)

    return rows


def get_row(line):
    a, b = 0, 127
    for x in line[:7]:
        c = a + (b - a) // 2
        if x == 'F':
            a, b = a, c
        elif x == 'B':
            a, b = c + 1, b
        else:
            raise ValueError
    return a


def get_col(line):
    a, b = 0, 7
    for x in line[7:]:
        c = a + (b - a) // 2
        if x == 'L':
            a, b = a, c
        elif x == 'R':
            a, b = c + 1, b
        else:
            raise ValueError
    return a


def test_convert():
    assert get_row('FBFBBFFRLR') == 44
    assert get_col('FBFBBFFRLR') == 5


def get_seat_id(boarding_pass):
    return 8 * get_row(boarding_pass) + get_col(boarding_pass)


def day_05_01():
    boarding_passes = get_data()
    return max([get_seat_id(boarding_pass) for boarding_pass in boarding_passes])


def test_day_05_01():
    assert day_05_01() == 878


def day_05_02():
    boarding_passes = get_data()
    reserved_seats = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]

    cols = set(get_col(boarding_pass) for boarding_pass in boarding_passes)
    rows = set(get_row(boarding_pass) for boarding_pass in boarding_passes)

    all_seats = []
    for r in rows:
        for c in cols:
            all_seats.append(8 * r + c)

    not_used = [x for x in all_seats if x not in reserved_seats]
    not_used = [x for x in not_used if x - 1 in reserved_seats]
    not_used = [x for x in not_used if x + 1 in reserved_seats]
    return not_used[0]


def test_day_05_02():
    assert day_05_02() == 504
