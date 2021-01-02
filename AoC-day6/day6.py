from string import ascii_lowercase

input_list = []
conn_input_list = []
letters_occ = []
counts_sum = 0

with open("day6") as file:
    for line in file:
        line = line.strip("\n")
        input_list.append(line)


inp_string = ""

for line in input_list:
    if line != "":
        inp_string = inp_string + line
    else:
        conn_input_list.append(inp_string)
        inp_string = ""

conn_input_list.append(inp_string)

for inp in conn_input_list:
    counter = 0
    for ch in ascii_lowercase:
        if ch in inp:
            counter += 1
    letters_occ.append(counter)

for nr in letters_occ:
    counts_sum += nr

print("Sum of these counts = {0}".format(counts_sum))

# part2

inp_2d_list = []
inp_1d_list = []
let_occ_all = []
new_counts_sum = 0

for line in input_list:
    if line != "":
        inp_1d_list.append(line)
    else:
        inp_2d_list.append(inp_1d_list)
        inp_1d_list = []

inp_2d_list.append(inp_1d_list)

for inp in inp_2d_list:
    counter = 0
    for ch in ascii_lowercase:
        local_counter = 0
        for string1 in inp:
            if ch in string1:
                local_counter += 1
            if local_counter == len(inp):
                counter += 1

    let_occ_all.append(counter)

for nr in let_occ_all:
    new_counts_sum += nr

print("New sum of counts = {0}".format(new_counts_sum))
