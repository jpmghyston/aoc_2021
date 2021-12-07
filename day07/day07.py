def get_input():
    with open("day07_input.txt") as f:
        return [int(x) for x in f.read().split(",")]


def simple_fuel_expenditure(start, end):
    return abs(end - start)


def triangle_fuel_expenditure(start, end):
    distance = abs(end - start)
    return int((distance * (distance + 1))/2)


def get_best_fuel(fuel_expenditure_method):
    crab_positions = get_input()
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    best_fuel = None
    best_position = None
    for i in range(min_position, max_position + 1):
        fuel_expenditure = 0
        for position in crab_positions:
            fuel_expenditure += fuel_expenditure_method(position, i)
        if best_fuel is None:
            best_fuel = fuel_expenditure
        else:
            if fuel_expenditure < best_fuel:
                best_fuel = fuel_expenditure
                best_position = i
    return best_fuel


def part_1():
    print(get_best_fuel(simple_fuel_expenditure))


def part_2():
    print(get_best_fuel(triangle_fuel_expenditure))


if __name__ == "__main__":
    part_1()
    part_2()