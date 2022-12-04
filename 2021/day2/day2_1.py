import fnmatch, re
import sys
sys.path.append('../')

import read_file

tup = read_file.get_file_contents('input')
# print(len(tup))
# print(type(tup))
# print(tup)



def get_horizontal_positions(input):
    # print("*** horizontal positions")
    dist_re = re.compile("^forward")

    distance = list(filter(dist_re.match, input))
    # print(distance)
    return distance


def get_depth_readings(input):
    # print("**** depth readings")
    depth_re = re.compile("^down|^up")
    depth = list(filter(depth_re.match, input))
    # print(depth)
    return depth

def convert_list_to_dict(list_arg):
    new_list = []
    for nested_list in list_arg:
        new_list.append(dict(zip(nested_list[::2], nested_list[1::2])))

    # print(new_list)
    return new_list

def split_instruction_from_readings(horizontal_reads : None, depth_reads : None):
    new_list = []
    if horizontal_reads != None:
        for reading in horizontal_reads:
            # discard 'forward' as it is not needed
            new_list.append(reading.split()[1])
    elif depth_reads != None:
        for reading in depth_reads:
            new_list.append(reading.split())

    # print(new_list)
    return new_list

def calculate_final_depth(input_list_of_dicts):
    depth = 0
    for input_dict in input_list_of_dicts:
        dict_item_list = next(iter(input_dict.items()))
        # print(dict_item_list)
        if dict_item_list[0] == "up":
            # print("up")
            depth = depth - int(dict_item_list[1])
        elif dict_item_list[0] == "down":
            # print("down")
            depth = depth + int(dict_item_list[1])
    print("depth = {}".format(depth))
    return depth

def calculate_dist_travelled(input_list):
    dist = 0
    for input in input_list:
        dist = dist + int(input)

    print("horizontal distance = {}".format(dist))
    return dist

horiz_pos_list = get_horizontal_positions(tup)
horiz_pos_list = split_instruction_from_readings(horiz_pos_list, None)
horiz_dist = calculate_dist_travelled(horiz_pos_list)


depth_list = get_depth_readings(tup)
depth_list = split_instruction_from_readings(None, depth_list)


depth_list_of_dicts = convert_list_to_dict(depth_list)
# print(depth_list_of_dicts)
depth = calculate_final_depth(depth_list_of_dicts)

final_position = depth * horiz_dist
print("final pos {}".format(final_position))

