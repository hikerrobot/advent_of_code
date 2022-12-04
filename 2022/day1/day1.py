import sys

sys.path.append('../../')

import read_file as rf

fileContents = rf.get_file_contents('input')
print("file lines = {}".format(len(fileContents)))

elf = 1
elf_calories_list = []
elf_cal_dict = {}
calories = 0
for line in fileContents:

    # print(line)
    if line == "":
        print("storing elf {} with calories {}".format(elf, calories))
        elf_cal_dict[elf] = calories
        elf += 1
        calories = 0
        continue
        
    calories += int(line)

# sort dict by value
sorted_dict = sorted(elf_cal_dict.items(), key=lambda item: item[1])
print(sorted_dict)