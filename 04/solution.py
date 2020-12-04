required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0
with open('input.txt') as f:
    lines = f.read()
    passports = [i.split() for i in lines.split('\n\n')]
    for passport in passports:
        fields = [i[:3] for i in passport]
        if all(req in fields for req in required_fields):
            valid_passports += 1

print(valid_passports)