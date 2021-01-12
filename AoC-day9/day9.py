def add_check(preamb_nr, inp_list, position):
    added_to = 0
    for i in range(position-preamb_nr - 1, position):
        for j in range(position-preamb_nr-1, position):
            if i == j:
                continue
            if inp_list[i] + inp_list[j] == inp_list[position]:
                added_to = 1
    return added_to


input_list = []

with open("day9") as file:
    for line in file:
        line = int(line.strip("\n"))
        input_list.append(line)

preamble_nr = 25

searched_number = None

for ind in range(preamble_nr+1, len(input_list)):
    if add_check(preamble_nr, input_list, ind) == 0:
        searched_number = input_list[ind]
        break

print("Searched number = {0}".format(searched_number))

# part2

min_index = None
max_index = None

for ctr in range(0, len(input_list)):
    nr_sum = 0
    for counter in range(ctr, len(input_list)):
        nr_sum += input_list[counter]
        if nr_sum == searched_number and ctr != counter:  # at least 2 numbers
            min_index = ctr
            max_index = counter
        if nr_sum > searched_number:
            break

list_from_searched = input_list[min_index:max_index+1]
smallest_from_searched = min(list_from_searched)
largest_from_searched = max(list_from_searched)

print("Sum of smallest and largest numbers in this range = {0}".format(smallest_from_searched+largest_from_searched))
