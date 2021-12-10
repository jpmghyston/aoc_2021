char_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

corruption_score_dict = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

autocomplete_score_dict = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def get_input():
    with open("day10_input.txt") as f:
        return [x.strip() for x in f.readlines()]


def get_corrption_score(line):
    stack = []
    for char in line:
        if char in char_dict.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return corruption_score_dict[char]
            elif char_dict[stack[-1]] != char:
                return corruption_score_dict[char]
            else:
                stack.pop()
    return 0


def get_autocomplete_score(line):
    stack = []
    for char in line:
        if char in char_dict.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return 0
            elif char_dict[stack[-1]] != char:
                return 0
            else:
                stack.pop()
    chars_to_add = [char_dict[char] for char in reversed(stack)]
    score = 0
    for char in chars_to_add:
        score *= 5
        score += autocomplete_score_dict[char]
    return score



def part_1():
    print(sum(get_corrption_score(line) for line in get_input()))

def part_2():
    autocomplete_scores = sorted(get_autocomplete_score(line) for line in get_input() if get_autocomplete_score(line) != 0)
    middle_score = autocomplete_scores[len(autocomplete_scores) // 2]
    print(middle_score)


if __name__ == "__main__":
    part_1()
    part_2()