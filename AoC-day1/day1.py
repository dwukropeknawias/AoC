my_list = []

with open("day1") as file:
    for line in file:
        line = int(line.strip("\n"))
        my_list.append(line)

for i in my_list:
    for j in my_list:
        if(i+j == 2020):
            print("Multiply of {0} and {1} = {2}".format(i, j, i*j))

#part 2

for i in my_list:
    for j in my_list:
        for k in my_list:
            if(i+j+k == 2020):
                print("Multiply of {0} and {1} and {2}= {3}".format(i, j, k, k*i*j))

