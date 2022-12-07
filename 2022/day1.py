import sys

sys.path.append('../')

import read_file as rf

fileContents = rf.get_file_contents('input-d1-work')
# print("file lines = {}".format(len(fileContents)))

elf = 1
elf_calories_list = []
elf_cal_dict = {}
calories = 0
for line in fileContents:

    # print(line)
    if line == "":
        # print("storing elf {} with calories {}".format(elf, calories))
        elf_cal_dict[elf] = calories
        elf += 1
        calories = 0
        continue
        
    calories += int(line)

# sort dict by value
# could've been better by using other than dict, as didn't need elf count as key
sorted_cal_list = sorted(elf_cal_dict.items(), key=lambda item: item[1])
last_idx = len(sorted_cal_list)-1
print("max calories for elf {}".format(sorted_cal_list[last_idx]))

# print(type(calories_list))
# print(calories_list[len(calories_list)-2:])

numElvesCals = 3
total_cals = 0
for i in range(len(sorted_cal_list)-numElvesCals, len(sorted_cal_list)):
    print(sorted_cal_list[i][1])
    total_cals += sorted_cal_list[i][1]

print("total cals {} for {} elves".format(total_cals, numElvesCals))