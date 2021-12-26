from itertools import chain

def get_input():
    with open("day13_input.txt") as f:
        input_array = [x.strip() for x in f.readlines()]
    qq = input_array.index("")
    coords = [[int(y) for y in x.split(",")] for x in input_array[:qq]]
    folds = input_array[qq+1:]
    return coords, folds

def print_coords(coords):
    max_x = max(x[0] for x in coords)
    max_y = max(x[1] for x in coords)
    map = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]
    for coord in coords:
        map[coord[1]][coord[0]] = "#"
    for line in map:
        print("".join(line))
    print("__")

def translate_coordinate(coord, axis, value):
    if axis == "x":
        if coord[0] < value:
            return (coord[0], coord[1])
        new_val = value - (coord[0] - value)
        return (new_val, coord[1])
    else:
        if coord[1] < value:
            return (coord[0], coord[1])
        new_val = value - (coord[1] - value)
        return (coord[0], new_val)

def part_1():
    coords, folds = get_input()
    # print_coords(coords)
    first_fold = folds[0]
    axis = "x" if "x" in first_fold else "y"
    value = int(first_fold.split("=")[1])
    # print_coords(new_coords)
    unique_coords = set([translate_coordinate(coord, axis, value) for coord in coords])
    print(len(unique_coords))

def part_2():
    coords, folds = get_input()
    for fold in folds:
        axis = "x" if "x" in fold else "y"
        value = int(fold.split("=")[1])
        coords = [translate_coordinate(coord, axis, value) for coord in coords]
    print_coords(coords)


if __name__ == "__main__":
    part_1()
    part_2()