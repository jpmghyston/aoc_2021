from itertools import chain

def get_input():
    with open("day08_input.txt") as f:
        return [line.strip().split("|") for line in f.readlines()]


def get_signals_with_length(signal_patterns, length):
    return [set(x) for x in signal_patterns if len(x) == length]


def get_letter_maps(signal_patterns):
    one_signal = get_signals_with_length(signal_patterns, 2)[0]
    four_signal = get_signals_with_length(signal_patterns, 4)[0]
    seven_signal = get_signals_with_length(signal_patterns, 3)[0]
    eight_signal = get_signals_with_length(signal_patterns, 7)[0]

    bottom_left_bars = eight_signal - (one_signal | four_signal | seven_signal)
    zero_six_signals = [x for x in get_signals_with_length(signal_patterns, 6) if len(x & bottom_left_bars) == 2]

    middle_right_bars = zero_six_signals[0] ^ zero_six_signals[1]
    middle_bar = middle_right_bars - one_signal
    zero_signal = [x for x in zero_six_signals if len(middle_bar & x) == 0][0]
    six_signal = [x for x in zero_six_signals if x != zero_signal][0]
    nine_signal = [x for x in get_signals_with_length(signal_patterns, 6) if x != zero_signal and x != six_signal][0]
    five_length_signals = get_signals_with_length(signal_patterns, 5)
    three_signal = [x for x in five_length_signals if len(x - one_signal) == 3][0]
    two_signal = [x for x in five_length_signals if len(bottom_left_bars & x) == 2][0]
    five_signal = [x for x in five_length_signals if x != three_signal and x != two_signal][0]
    return {
        frozenset(zero_signal): "0",
        frozenset(one_signal): "1",
        frozenset(two_signal): "2",
        frozenset(three_signal): "3",
        frozenset(four_signal): "4",
        frozenset(five_signal): "5",
        frozenset(six_signal): "6",
        frozenset(seven_signal): "7",
        frozenset(eight_signal): "8",
        frozenset(nine_signal): "9"
    }


def part_1():
    vals = get_input()
    vals_to_consider = chain.from_iterable([val[1].split(" ") for val in vals])
    lens_to_consider = set([2, 3, 4, 7])
    count_unique_vals = 0
    for val in vals_to_consider:
        if len(val) in lens_to_consider:
            count_unique_vals += 1
    print(count_unique_vals)


def part_2():
    vals = get_input()
    total = 0
    for val in vals:
        letter_map = get_letter_maps(val[0].split(" "))
        output_vals = [letter_map[frozenset(x)] for x in val[1].strip().split(" ")]
        total += int("".join(output_vals))
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()