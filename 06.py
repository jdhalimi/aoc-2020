INPUT = '06.txt'


def get_data():
    rows = []
    with open(INPUT) as f:
        for line in f:
            line = line.strip()
            rows.append(line)

    return rows


def day_06_1():
    data = get_data()
    questions = set()
    result = 0
    while True:
        line = data.pop(0)
        if line:
            for c in line:
                questions.add(c)
        else:
            result += len(questions)
            questions = set()

        if not data:
            n = len(questions)
            result += n
            return result


def test_day_06_01():
    assert day_06_1() == 6549


def day_06_2():
    data = get_data()
    questions = {}
    people = 0
    result = 0
    while True:
        line = data.pop(0)
        if line:
            people += 1
            for c in line:
                questions[c] = questions.get(c, 0) + 1
        else:
            result += len([c for c, v in questions.items() if v == people])
            questions = {}
            people = 0

        if not data:
            result += len([c for c, v in questions.items() if v == people])
            return result


def test_day_06_2():
    assert day_06_2() == 6549
