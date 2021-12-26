def get_input():
    with open("day14_input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    initial = lines[0]
    rules_list = [x.split(" -> ") for x in lines[2:]]
    rules_dict = {}
    for rule in rules_list:
        rules_dict[rule[0]] = rule[1]
    return initial, rules_dict

def apply_step(template, rules):
    new_template = ""
    for i in range(len(template)-1):
        pair = "".join([template[i], template[i+1]])
        new_last = rules[pair]
        new_template += pair[0]
        new_template += new_last
    new_template += pair[1]
    return new_template

def increment_pair(pair_counts, pair, inc_by):
    if pair in pair_counts:
        pair_counts[pair] += inc_by
    else:
        pair_counts[pair] = inc_by

def decrement_or_delete_pair(pair_counts, pair):
    if pair_counts[pair] <= 1:
        pair_counts.pop(pair)
    else:
        pair_counts[pair] -= 1

def apply_step_optimised(pair_counts, rules, char_counts):
    init_pair_counts = pair_counts.copy()
    new_pair_counts = pair_counts.copy()
    for pair in pair_counts:
        inc_by = init_pair_counts[pair]
        new = rules[pair]
        if new in char_counts:
            char_counts[new] += inc_by
        else:
            char_counts[new] = inc_by
        pair_1, pair_2 = pair[0] + rules[pair], rules[pair] + pair[1]
        increment_pair(new_pair_counts, pair_1, inc_by)
        increment_pair(new_pair_counts, pair_2, inc_by)
        increment_pair(new_pair_counts, pair, inc_by * -1)
    return new_pair_counts

def part_1():
    template, rules = get_input()
    for i in range(10):
        template = apply_step(template, rules)
        # print(i, template)
    letters = set(x for x in template)
    letter_counts = []
    for letter in letters:
        letter_counts.append(template.count(letter))
    print(max(letter_counts) - min(letter_counts))

def get_pair_counts(template):
    pair_counts = {}
    for i in range(len(template)-1):
        pair = "".join([template[i], template[i+1]])
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1
    return pair_counts

def part_2():
    template, rules = get_input()
    pair_counts = get_pair_counts(template)
    char_counts = {}
    for char in template:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for i in range(40):
        pair_counts = apply_step_optimised(pair_counts, rules, char_counts)
    print(max(char_counts.values()) - min(char_counts.values()))

if __name__ == "__main__":
    part_1()
    part_2()