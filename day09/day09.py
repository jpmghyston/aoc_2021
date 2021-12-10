def get_input():
    with open("day09_input.txt") as f:
        return [[int(y) for y in x.strip()] for x in f.readlines()]


def get_low_points(heatmap):
    max_i = len(heatmap)
    max_j = len(heatmap[0])
    for i in range(max_i):
        for j in range(max_j):
            cur_height = heatmap[i][j]
            adjacent_heights = []
            if i > 0:
                adjacent_heights.append(heatmap[i-1][j])
            if i < max_i - 1 and heatmap[i+1][j] < cur_height:
                adjacent_heights.append(heatmap[i+1][j])
            if j > 0:
                adjacent_heights.append(heatmap[i][j-1])
            if j < max_j - 1:
                adjacent_heights.append(heatmap[i][j + 1])
            if all(height > cur_height for height in adjacent_heights):
                yield cur_height, i, j


def get_basin_sizes(heatmap, low_points):
    max_i = len(heatmap)
    max_j = len(heatmap[0])
    return 0


def part_1():
    heatmap = get_input()
    print(sum(point[0] + 1 for point in get_low_points(heatmap)))


def part_2():
    heatmap = get_input()
    low_points = [[point, 0] for point in get_low_points(heatmap)]


if __name__ == "__main__":
    part_1()
    part_2()