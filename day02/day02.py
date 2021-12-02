
def get_input():
    with open("day02_input.txt") as f:
        input_data = f.readlines()
    return [x.split(" ") for x in input_data]


def part_1():
    instructions = get_input()
    depth = 0
    horizontal = 0
    for instruction in instructions:
        dist = int(instruction[1])
        if instruction[0] == "forward":
            horizontal += dist
        elif instruction[0] == "down":
            depth += dist
        elif instruction[0] == "up":
            depth -= dist
    print(depth*horizontal)


def part_2():
    instructions = get_input()
    depth = 0
    horizontal = 0
    aim = 0
    for instruction in instructions:
        dist = int(instruction[1])
        if instruction[0] == "forward":
            horizontal += dist
            depth += aim * dist
        elif instruction[0] == "down":
            aim += dist
        elif instruction[0] == "up":
            aim -= dist
    print(depth*horizontal)


if __name__ == '__main__':
    part_1()
    part_2()

