from functools import reduce

def get_input():
    with open("day03_input.txt") as f:
        input_data = f.readlines()
    return [[int(y) for y in x.strip()] for x in input_data]

def part_1():
    vals = get_input()
    total_num_of_nums = len(vals)
    len_of_each_num = len(vals[0])
    bitwise_val_counts = [0 for x in range(len_of_each_num)]
    for val in vals:
        for i in range(len_of_each_num):
            bitwise_val_counts[i] += val[i]
    bitwise_gamma = [None for x in range(len_of_each_num)]
    bitwise_epsilon = [None for x in range(len_of_each_num)]
    for i in range(len_of_each_num):
        if bitwise_val_counts[i] > total_num_of_nums/2:
            bitwise_gamma[i] = "1"
            bitwise_epsilon[i] = "0"
        else:
            bitwise_gamma[i] = "0"
            bitwise_epsilon[i] = "1"
    print(int("".join(bitwise_gamma), 2) * int("".join(bitwise_epsilon), 2))


if __name__ == '__main__':
    part_1()
