from functools import reduce

def get_input():
    with open("day03_input.txt") as f:
        input_data = f.readlines()
    return [[int(y) for y in x.strip()] for x in input_data]

def part_1(vals):
    total_num_of_nums = len(vals)
    len_of_each_num = len(vals[0])
    bitwise_val_counts = [0 for x in range(len_of_each_num)]
    for val in vals:
        for i in range(len_of_each_num):
            bitwise_val_counts[i] += val[i]
    bitwise_gamma = [None for x in range(len_of_each_num)]
    bitwise_epsilon = [None for x in range(len_of_each_num)]
    for i in range(len_of_each_num):
        if bitwise_val_counts[i] >= total_num_of_nums/2:
            bitwise_gamma[i] = "1"
            bitwise_epsilon[i] = "0"
        else:
            bitwise_gamma[i] = "0"
            bitwise_epsilon[i] = "1"
    return bitwise_gamma, bitwise_epsilon


def part_2():
    possible_oxygen_gen_ratings = get_input()
    possible_co2_scrubber_ratings = get_input()

    pos = 0
    while len(possible_oxygen_gen_ratings) > 1:
        bitwise_gamma, _ = part_1(possible_oxygen_gen_ratings)
        possible_oxygen_gen_ratings = [x for x in possible_oxygen_gen_ratings if x[pos] == int(bitwise_gamma[pos])]
        pos += 1

    pos = 0
    while len(possible_co2_scrubber_ratings) > 1:
        _, bitwise_epsilon = part_1(possible_co2_scrubber_ratings)
        possible_co2_scrubber_ratings = [x for x in possible_co2_scrubber_ratings if x[pos] == int(bitwise_epsilon[pos])]
        pos += 1

    oxygen_rating = int("".join([str(x) for x in possible_oxygen_gen_ratings[0]]), 2)
    co2_rating = int("".join([str(x) for x in possible_co2_scrubber_ratings[0]]), 2)

    print(oxygen_rating * co2_rating)


if __name__ == '__main__':
    bitwise_gamma, bitwise_epsilon = part_1(get_input())
    print(int("".join(bitwise_gamma), 2) * int("".join(bitwise_epsilon), 2))
    part_2()
