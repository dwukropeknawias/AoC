def bags_finder(inp_list, bag_type, bags_list=[]):
    corrected_input_list = []
    for inp in inp_list:
        if (bag_type + " bags contain") not in inp:
            corrected_input_list.append(inp)

    for bag_str in corrected_input_list:
        if bag_type in bag_str:
            temp = bag_str.split()
            next_bag_type = temp[0] + " " + temp[1]
            bags_list.append(next_bag_type)
            bags_finder(inp_list, next_bag_type, bags_list)
            if "no other bags" in bag_str:
                return bags_list
    return bags_list

# part2 function

def bag_container(inp_list, bag_type, counter_list=[], multiply=1):
    for inp in inp_list:
        if (bag_type + " bags contain") in inp:
            temp_list = inp.split()[4:]
            if "no" in temp_list:
                return counter_list
            i = 0
            while i < len(temp_list):
                counter_list.append(int(temp_list[i])*multiply)
                temp_mult = multiply
                multiply = int(temp_list[i])*multiply
                next_bag = temp_list[i+1] + " " + temp_list[i+2]
                bag_container(inp_list, next_bag, counter_list, multiply)
                multiply = temp_mult
                i += 4

    return counter_list


input_list = []

with open("day7") as file:
    for line in file:
        line = line.strip("\n")
        input_list.append(line)


all_bags = (bags_finder(input_list, "shiny gold"))
all_bags_without_repeat = set(all_bags)

print("One shiny gold bag can contain {0} bag colors. ".format(len(all_bags_without_repeat)))

# part2

bag_sum = sum(bag_container(input_list, "shiny gold"))

print("Inside shiny gold bag are required {0} individual bags.".format(bag_sum))



