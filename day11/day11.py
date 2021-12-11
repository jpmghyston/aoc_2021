from itertools import chain


def get_input():
    with open("day11_input.txt") as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def increase_energy_levels(map):
    return [[level + 1 for level in line] for line in map]


def has_octopus_ready_to_flash(map):
    return any(level > 9 for level in chain.from_iterable(map))


def all_are_synchronised(map):
    return all(level == 0 for level in chain.from_iterable(map))


def process_flashes(map):
    new_map = [line.copy() for line in map.copy()]
    max_i = len(new_map)
    max_j = len(new_map[0])
    flash_count = 0
    while has_octopus_ready_to_flash(new_map):
        for i in range(max_i):
            for j in range(max_j):
                if new_map[i][j] > 9:
                    new_map[i][j] = 0
                    flash_count += 1
                    for x in (_ for _ in range(i - 1, i + 2) if _ >= 0 and _ < max_i):
                        for y in (_ for _ in range(j - 1, j + 2) if _ >= 0 and _ < max_j):
                            if new_map[x][y] != 0:
                                new_map[x][y] += 1

    return new_map, flash_count


def print_map(map):
    for line in map:
        print("".join(str(x if x < 10 else "X") for x in line))
    print("")



def part_1():
    map = get_input()
    flash_count = 0
    for _ in range(100):
        # print_map(map)
        map = increase_energy_levels(map)
        map, new_flashes = process_flashes(map)
        flash_count += new_flashes
    print(flash_count)


def part_2():
    map = get_input()
    step_count = 0
    while not all_are_synchronised(map):
        print_map(map)
        map = increase_energy_levels(map)
        map, _ = process_flashes(map)
        step_count += 1
    print(step_count)


if __name__ == "__main__":
    part_1()
    part_2()