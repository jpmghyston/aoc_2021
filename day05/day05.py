from itertools import chain

def get_input():
    with open("day05_input.txt") as f:
        input_data = f.readlines()
    lines = []
    for entry in input_data:
        left, right = entry.split(" -> ")
        coords = [[int(x) for x in left.split(",")], [int(y) for y in right.split(",")]]
        lines.append(coords)
    return lines


def line_is_horizontal_or_vertical(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def coords_are_equal(first, second):
    return first[0] == second[0] and first[1] == second[1]


def part_1():
    lines = get_input()
    lines_to_consider = [line for line in lines if line_is_horizontal_or_vertical(line)]
    map = generate_map(lines_to_consider)
    print(len([x for x in chain.from_iterable(map) if x > 1]))


def generate_map(lines_to_consider):
    map_size = 1000
    map = [[0 for _ in range(map_size)] for _ in range(map_size)]
    for start, end in lines_to_consider:
        coord = start
        map[coord[1]][coord[0]] += 1
        while not coords_are_equal(coord, end):
            if coord[0] < end[0]:
                coord[0] += 1
            elif coord[0] > end[0]:
                coord[0] -= 1
            if coord[1] < end[1]:
                coord[1] += 1
            elif coord[1] > end[1]:
                coord[1] -= 1
            map[coord[1]][coord[0]] += 1
    return map


def part_2():
    map_size = 1000
    lines = get_input()
    map = generate_map(lines)
    print(len([x for x in chain.from_iterable(map) if x > 1]))


if __name__ == '__main__':
    part_1()
    part_2()
