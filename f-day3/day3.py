from math import ceil


def split(word):
    return [c for c in word]


my_list = []
counter = 0

with open("day3") as file:
    for line in file:
        line = split(line)
        line = line[:-1]
        my_list.append(line)


min_length = 7*(len(my_list)-1)+1 #changed from 3 to 7(max) in part2 for bigger map
repeat = ceil(min_length/len(my_list[0]))

repeat_times = 0

if repeat > 1:
    repeat_times = repeat - 1
else:
    repeat_times = repeat

temp_list = my_list

i = 1
while i <= repeat_times:

    my_list = [x + y for x, y in zip(my_list, temp_list)]
    i += 1

j = 1
indx = 3
while j < len(my_list):
    if my_list[j][indx] == "#":
        counter += 1
    j += 1
    indx += 3

print("Part 1: {0}".format(counter))

#part 2

counter11, counter51, counter71, counter12 = 0, 0, 0, 0

j11 = 1
indx11 = 1
while j11 < len(my_list):
    if my_list[j11][indx11] == "#":
        counter11 += 1
    j11 += 1
    indx11 += 1

print("Right 1, down 1 : {0}".format(counter11))

j51 = 1
indx51 = 5
while j51 < len(my_list):
    if my_list[j51][indx51] == "#":
        counter51 += 1
    j51 += 1
    indx51 += 5

print("Right 5, down 1 : {0}".format(counter51))

j71 = 1
indx71 = 7
while j71 < len(my_list):
    if my_list[j71][indx71] == "#":
        counter71 += 1
    j71 += 1
    indx71 += 7

print("Right 7, down 1 : {0}".format(counter71))

j12 = 2
indx12 = 1
while j12 < len(my_list):
    if my_list[j12][indx12] == "#":
        counter12 += 1
    j12 += 2
    indx12 += 1

print("Right 1, down 2 : {0}".format(counter12))

print("Multiply of all: {0}".format(counter * counter11 * counter51 * counter71 * counter12))


