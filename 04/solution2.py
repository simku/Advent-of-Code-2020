import re

required_fields = {'byr': lambda x: 1920 <= int(x) <= 2002,
                   'iyr': lambda x: 2010 <= int(x) <= 2020,
                   'eyr': lambda x: 2020 <= int(x) <= 2030,
                   'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
                   'hcl': lambda x: len(x) == 7 and re.match(r'^#[0-9a-f]+$', x),
                   'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                   'pid': lambda x: len(x) == 9 and x.isnumeric()}

passport = []
valid_passports = 0
with open('input.txt') as f:
    lines = f.read()
    passports = [i.split() for i in lines.split('\n\n')]
    for passport in passports:
        passport = list(filter(lambda field: field[:3] in required_fields, passport))
        if len(passport) == 7 and all([required_fields[field[:3]](field[4:]) for field in passport]):
            valid_passports += 1

print(valid_passports)