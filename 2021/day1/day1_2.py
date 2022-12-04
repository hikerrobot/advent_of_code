import sys
sys.path.append('../')

import read_file

increase = 0
totalsDict = {}
measurement_windows_list = []
window_totals_list = []

def sum_window(measurement_list):
    print(measurement_list)
    total = 0
    for measurement in measurement_list:
        total = total + int(measurement)
    print("measurement window total = {}".format(total))
    return total

def process_measurements(windows_total_list):

    increase = 0
    print("list size = {}".format(len(window_totals_list)))

    for i in range (0, len(windows_total_list)-1):
        curr_measurement = windows_total_list[i]
        next_measurement = windows_total_list[i+1]
        print("{}: curr_measurement {}, next measurement {}".format(i, curr_measurement, next_measurement))

        if (next_measurement > curr_measurement):
            print("increase")
            increase = increase +1 

        # if i > 10:
        #     break

    print("total increases = {}".format(increase))


def create_windows(measurement_list):

    measurement_windows = []
    for measurement_index in range(0, len(measurement_list)):
        if measurement_index + 3 > len(measurement_list):
            break
        # slice the list to get the required windows
        measurement_windows.append(measurement_list[measurement_index:measurement_index+3])

    # print(measurement_window
    # s)
    return measurement_windows

puzzle_input = read_file.get_file_contents('input')
halt_early = True
halt_index = 9


# sys.exit(0)

measurement_windows_list = create_windows(puzzle_input)

for measurement_window in measurement_windows_list:
    window_totals_list.append(sum_window(measurement_window))

# print(window_totals_list)
# print(len(window_totals_list))

process_measurements(window_totals_list)


# print("increased measurements = {0}".format(increase))




