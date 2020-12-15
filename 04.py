import re

INPUT = '04.txt'

FIELDS = ['byr',
          'iyr',
          'eyr',
          'hgt',
          'hcl',
          'ecl',
          'pid',
          'cid']

ECL_LIST = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

OPTIONAL_FIELDS = ['cid']

HGT_PATTERN = re.compile(r'(\d+)(in|cm)')
HCL_PATTERN = re.compile(r'#[0-9a-f]{6}')


def get_data():
    passports = []
    current = {}
    with open(INPUT) as f:
        for line in f:
            line = line.strip()
            if not line:
                if current:
                    passports.append(current)
                current = {}

            else:
                for data in line.split():
                    k, v = data.split(':', 1)
                    current[k] = v
    return passports


def is_valid_passport(passport, strict=False):
    for field in FIELDS:
        if field not in passport:
            if field not in OPTIONAL_FIELDS:
                return False

    if strict:

        y = int(passport['byr'])
        if not 1920 <= y <= 2002:
            return False

        y = int(passport['iyr'])
        if not 2010 <= y <= 2020:
            return False

        y = int(passport['eyr'])
        if not 2020 <= y <= 2030:
            return False

        m = HGT_PATTERN.match(passport['hgt'])
        if not m:
            return False
        else:
            x, u = m.groups()
            x = int(x)
            if u == "cm" and not 150 <= x <= 193:
                return False
            if u == "in" and not 59 <= x <= 76:
                return False

        if not HCL_PATTERN.match(passport['hcl']):
            return False

        if passport['ecl'] not in ECL_LIST:
            return False

        if len(passport['pid']) != 9:
            return False

    return True


def day_04_01():
    passports = get_data()
    valid_passports = [passport for passport in passports if is_valid_passport(passport, strict=False)]
    return len(valid_passports)


def day_04_02():
    passports = get_data()
    valid_passports = [passport for passport in passports if is_valid_passport(passport, strict=True)]
    return len(valid_passports)


def test_re_pattern():
    assert HGT_PATTERN.match("125cm").groups() == ('125', 'cm')

    assert HCL_PATTERN.match("#123456a")
    assert HCL_PATTERN.match("#123456b")
    assert not HCL_PATTERN.match("12345b")


def test_day_04_01():
    assert day_04_01() == 256


def test_day_04_05():
    assert day_04_02() == 198
