import re

my_list = []
valid_counter = 0
fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
new_list = []

with open("day4") as file:
    for line in file:
        line = line.strip()
        my_list.append(line)


string = ""

for line in my_list:
    if line != "":
        string = string + " " + line
    else:
        new_list.append(string)
        string = ""

new_list.append(string)

for str_f in new_list:
    if all(x in str_f for x in fields):
        valid_counter += 1

print("Valid passports = {0}".format(valid_counter))

#part 2

valid2_counter = 0
temp_fields_list = []

byr_rgx = r"(192[0-9]|19[3-9][0-9]|200[0-2])"
iyr_rgx = r"^(201[0-9]|2020)$"
eyr_rgx = r"^(202[0-9]|2030)$"
hgt_rgx = r"^((15[0-9]|1[6-8][0-9]|19[0-3])cm$)|((^59|6[0-9]|7[0-6])in)$"
hcl_rgx = r"^[#][0-9a-f]{6}$"
ecl_rgx = r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$"
pid_rgx = r"^[0-9]{9}$"

for str_f in new_list:
    if all(x in str_f for x in fields):
        temp_fields_list = str_f.split()
        byr = [s for s in temp_fields_list if "byr" in s][0][4:]
        iyr = [s for s in temp_fields_list if "iyr" in s][0][4:]
        eyr = [s for s in temp_fields_list if "eyr" in s][0][4:]
        hgt = [s for s in temp_fields_list if "hgt" in s][0][4:]
        hcl = [s for s in temp_fields_list if "hcl" in s][0][4:]
        ecl = [s for s in temp_fields_list if "ecl" in s][0][4:]
        pid = [s for s in temp_fields_list if "pid" in s][0][4:]

        if re.match(byr_rgx, byr) and re.match(iyr_rgx, iyr) and re.match(eyr_rgx, eyr) and re.match(hgt_rgx, hgt)\
                and re.match(hcl_rgx, hcl) and re.match(ecl_rgx, ecl) and re.match(pid_rgx, pid):
            valid2_counter += 1


print("New valid passports = {0}".format(valid2_counter))
