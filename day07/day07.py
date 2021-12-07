def get_input():
    with open("day07_input.txt") as f:
        return [int(x) for x in f.read().split(",")]


def part_1():
    crab_positions = get_input()
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    best_fuel = None
    best_position = None
    for i in range(min_position, max_position + 1):
        fuel_expenditure = 0
        for position in crab_positions:
            fuel_expenditure += abs(position - i)
        if best_fuel is None:
            best_fuel = fuel_expenditure
        else:
            if fuel_expenditure < best_fuel:
                best_fuel = fuel_expenditure
                best_position = i
    print(best_fuel)


def part_2():
    crab_positions = get_input()
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    best_fuel = None
    best_position = None
    for i in range(min_position, max_position + 1):
        fuel_expenditure = 0
        for position in crab_positions:
            distance = abs(position - i)
            fuel_expenditure += (distance * (distance + 1))/2
        if best_fuel is None:
            best_fuel = fuel_expenditure
        else:
            if fuel_expenditure < best_fuel:
                best_fuel = fuel_expenditure
                best_position = i
    print(best_fuel)


if __name__ == "__main__":
    part_1()
    part_2()