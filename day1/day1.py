
def get_depths():
    with open("day1_input.txt") as f:
        input_data = f.readlines()
    return [int(x) for x in input_data]


def get_increase_count(depths):
    last_depth = None
    increase_count = 0
    for depth in depths:
        if last_depth is not None and last_depth < depth:
            increase_count += 1
        last_depth = depth
    return increase_count


def get_windowed_depths(depths):
    window = []
    windowed_sums = []
    for depth in depths:
        window.append(depth)
        if len(window) > 3:
            window.pop(0)
        if len(window) == 3:
            windowed_sums.append(sum(window))
    return windowed_sums


def part_1():
    print(get_increase_count(get_depths()))


def part_2():
    print(get_increase_count(get_windowed_depths(get_depths())))


if __name__ == '__main__':
    part_1()
    part_2()

