from itertools import chain

def get_input():
    with open("day04_input.txt") as f:
        input_data = f.readlines()

    draw_numbers = [int(x) for x in input_data[0].split(",")]

    board_data = input_data[2:]
    boards = []
    current_board = []
    for line in board_data:
        if line == "\n":
            boards.append(current_board.copy())
            current_board = []
        else:
            current_board.append([[int(x), False] for x in line.strip().split(" ") if x != ""])
    boards.append(current_board)
    return draw_numbers, boards


def mark_number(board, number):
    for row in board:
        for element in row:
            if element[0] == number:
                element[1] = True


def has_bingo(board):
    for row in board:
        if all(element[1] for element in row):
            return True
    columns = []
    for i in range(5):
        columns.append([board[x][i] for x in range(5)])
    for column in columns:
        if all(element[1] for element in column):
            return True
    return False


def board_score(board, num):
    chained_board = [x for x in chain.from_iterable(board)]
    filtered_board = [x[0] for x in chained_board if x[1] == False]
    return sum(filtered_board) * num


def part_1():
    draw_numbers, boards = get_input()
    for num in draw_numbers:
        for board in boards:
            mark_number(board, num)
            if has_bingo(board):
                print(board_score(board, num))
                return


def part_2():
    draw_numbers, boards = get_input()
    for num in draw_numbers:
        for board in boards:
            mark_number(board, num)
            if all(has_bingo(x) for x in boards):
                print(board_score(board, num))
                return


if __name__ == '__main__':
    part_1()
    part_2()
