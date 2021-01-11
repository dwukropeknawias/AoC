

def is_terminating(inp_list):
    termination = 0
    index_list = []
    accumulator = 0
    index = 0
    target = []

    while index < len(inp_list):
        value = inp_list[index]
        num = int(value[5:])
        if "acc" in value:
            if index in index_list:
                termination = 1
                break
            index_list.append(index)
            index += 1
            if value[4] == "+":
                accumulator += num
            else:
                accumulator -= num
        elif "jmp" in value:
            if index in index_list:
                termination = 1
                break
            index_list.append(index)

            if value[4] == "+":
                index += num
            else:
                index -= num

        elif "nop" in value:
            if index in index_list:
                termination = 1
                break
            index_list.append(index)
            index += 1
    target.append(accumulator)
    target.append(termination)
    # print("Accumulator = {0} ".format(accumulator))
    return target


input_list = []

with open("day8") as file:
    for line in file:
        line = line.strip("\n")
        input_list.append(line)


print(is_terminating(input_list))


# part2

for ind, val in enumerate(input_list):
    temp_list = input_list.copy()
    if "jmp" in val:
        new_str = "nop" + val[3:]
        temp_list[ind] = new_str
    elif "nop" in val:
        new_str = "jmp" + val[3:]
        temp_list[ind] = new_str
    if is_terminating(temp_list)[1] == 0:
        print("Accumulator without inf loop = {0} ".format(is_terminating(temp_list)[0]))
