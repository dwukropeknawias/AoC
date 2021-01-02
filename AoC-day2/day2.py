my_list = []

with open("day2") as file:
    for line in file:
        line = line.strip("\n")
        my_list.append(line)

counter = 0

for my_string in my_list:

    arr = my_string.split(" ")
    limit = arr[0].split("-")
    lower_limit = int(limit[0])
    upper_limit = int(limit[1])
    check_char = arr[1].replace(":","")
    the_string = arr[2]

    checker = the_string.count(check_char)

    if lower_limit <= checker <= upper_limit:
        counter += 1

print(counter)

#part 2

counter2 = 0

for my_string in my_list:

    arr = my_string.split(" ")
    place = arr[0].split("-")
    first_place = int(place[0])
    second_place = int(place[1])
    check_char = arr[1].replace(":", "")
    the_string = arr[2]

    if (the_string[first_place-1] == check_char and the_string[second_place-1] != check_char) or (the_string[first_place-1] != check_char and the_string[second_place-1] == check_char):
        counter2 += 1

print(counter2)