INPUT = '01.txt'


def get_data():
    with open(INPUT) as f:
        numbers = [int(x) for x in f]
    numbers.sort()
    return numbers


def find(numbers, s=0):
    for i, x in enumerate(numbers):
        for y in numbers[i + 1:]:
            if x + y == s:
                return x, y
    raise ValueError


def day_01_1():
    numbers = get_data()
    x, y = find(numbers, 2020)
    return x * y


def day_01_2():
    numbers = get_data()

    for i, x in enumerate(numbers):
        try:
            y, z = find(numbers[i + 1:], 2020 - x)
            return x * y * z
        except ValueError:
            pass


def test_day_01_01():
    assert day_01_1() == 32064


def test_day_01_02():
    assert day_01_2() == 193598720


if __name__ == '__main__':
    print('1.1: ', day_01_1())
    print('1.2: ', day_01_2())
