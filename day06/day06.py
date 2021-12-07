def get_input():
    with open("day06_input.txt") as f:
        input_data = f.read()
    return [int(x) for x in input_data.split(",")]


def part1():
    fishes = get_input()
    days_to_simulate = 80
    for day in range(days_to_simulate):
        new_fishes = []
        for i in range(len(fishes)):
            fishes[i] -= 1
            if fishes[i] < 0:
                fishes[i] = 6
                new_fishes.append(8)
        fishes.extend(new_fishes)
    print(len(fishes))


def part2():
    fishes = get_input()
    fish_counts = [0 for i in range(9)]
    for i in range(9):
        num_fish_with_count = len([x for x in fishes if x == i])
        fish_counts[i] = num_fish_with_count
    days_to_simulate = 256
    for day in range(days_to_simulate):
        new_fishes = fish_counts[0]
        fish_counts = fish_counts[1:]
        fish_counts[6] += new_fishes
        fish_counts.append(new_fishes)
    print(sum(fish_counts))


if __name__ == "__main__":
    part1()
    part2()