import itertools

my_list = []

with open("day5") as file:
    for line in file:
        line = line.strip("\n")
        my_list.append(line)

max_seat_id = 0

for board_pass in my_list:

    lower_row = 0
    upper_row = 127
    sum_between_rows = upper_row - lower_row + 1

    for i in range(7):
        if board_pass[i] == "F":
            sum_between_rows /= 2
            upper_row = upper_row - sum_between_rows
        else:
            sum_between_rows /= 2
            lower_row = lower_row + sum_between_rows

    final_row = int(lower_row)  # same as upper_row now

    lower_column = 0
    upper_column = 7
    sum_between_columns = upper_column - lower_column + 1

    for i in range(7, 10):
        if board_pass[i] == "L":
            sum_between_columns /= 2
            upper_column = upper_column - sum_between_columns
        else:
            sum_between_columns /= 2
            lower_column = lower_column + sum_between_columns

    final_column = int(lower_column)

    seat_ID = final_row * 8 + final_column

    if seat_ID > max_seat_id:
        max_seat_id = seat_ID

print("Highest seat ID = {0}".format(max_seat_id))

# part2

my_seat_ID = None

rows = ["".join(x) for x in itertools.product('FB', repeat=7)]

columns = ["".join(x) for x in itertools.product('LR', repeat=3)]

all_board_passes = ["".join(x) for x in itertools.product(rows, columns, repeat=1)]

missing_board_passes = [x for x in all_board_passes if x not in my_list]

missing_board_passes_ID = []

for board_pass in missing_board_passes:

    lower_row = 0
    upper_row = 127
    sum_between_rows = upper_row - lower_row + 1

    for i in range(7):
        if board_pass[i] == "F":
            sum_between_rows /= 2
            upper_row = upper_row - sum_between_rows
        else:
            sum_between_rows /= 2
            lower_row = lower_row + sum_between_rows

    final_row = int(lower_row)

    lower_column = 0
    upper_column = 7
    sum_between_columns = upper_column - lower_column + 1

    for i in range(7, 10):
        if board_pass[i] == "L":
            sum_between_columns /= 2
            upper_column = upper_column - sum_between_columns
        else:
            sum_between_columns /= 2
            lower_column = lower_column + sum_between_columns

    final_column = int(lower_column)

    seat_ID = final_row * 8 + final_column

    missing_board_passes_ID.append(seat_ID)


for i in range(1, len(missing_board_passes_ID) - 1):
    if (missing_board_passes_ID[i-1] != missing_board_passes_ID[i] - 1) and \
            (missing_board_passes_ID[i+1] != missing_board_passes_ID[i] + 1):
        my_seat_ID = missing_board_passes_ID[i]

print("My seat ID = {0}".format(my_seat_ID))
