import re

nonempty_pattern = r'^([\w|\s]+) bags contain (.*)$'
empty_pattern = r'^([\w|\s]+) bags contain no other bags'
rule_pattern = r'(\d) ([\w|\s]+) bag[s.]*'


def count_bags(bag, rules):
    if bag not in rules or not rules[bag]:
        return 1
    sum = 0
    for inner_bag in rules[bag]:
        sum += inner_bag['amount'] * count_bags(inner_bag['type'], rules)
    return sum + 1


rules = {}
for line in open('input.txt', 'r'):
    match = re.match(empty_pattern, line)
    if match:
        rules[match.group(1)] = []
        continue
    match = re.match(nonempty_pattern, line)
    bag = match.group(1)
    inner_bags = match.group(2).split(', ')
    bag_rules = []
    for inner_bag in inner_bags:
        match = re.match(rule_pattern, inner_bag)
        amount = int(match.group(1))
        bag_type = match.group(2)
        bag_rules.append({'amount': amount, 'type': bag_type})
    rules[bag] = bag_rules

bags_inside_shiny_gold = count_bags('shiny gold', rules) - 1
print(bags_inside_shiny_gold)