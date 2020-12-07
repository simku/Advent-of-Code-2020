import re

nonempty_pattern = r'^([\w|\s]+) bags contain (.*)$'
empty_pattern = r'^([\w|\s]+) bags contain no other bags'
rule_pattern = r'(\d) ([\w|\s]+) bag[s.]*'


def contains_gold(bag, rules):
    if bag not in rules:
        return False
    if 'shiny gold' in rules.get(bag):
        return True
    else:
        inner_bags = rules.get(bag)
        new_rules = rules.copy()
        new_rules.pop(bag)
        for inner_bag in inner_bags:
            if contains_gold(inner_bag, new_rules):
                return True
        return False


rules = {}
for line in open('input.txt', 'r'):
    match = re.match(empty_pattern, line)
    if match:
        rules[match.group(1)] = []
        continue
    match = re.match(nonempty_pattern, line)
    bag = match.group(1)
    inner_bags = match.group(2).split(', ')
    rules[bag] = [re.match(rule_pattern, inner_bag).group(2) for inner_bag in inner_bags]

bags_with_gold = sum([contains_gold(bag, rules) for bag in rules])
print(bags_with_gold)