import sys
sys.path.append('../')

import read_file

tup = read_file.get_file_contents('input')
print(type(tup))

increase = 0
for measurement in range(1, len(tup)):
    print(measurement)
    next_measurement = int(tup[measurement])
    curr_measurement = int(tup[measurement-1])
    # print(type(curr_measurement))
    print("is {0} > {1}".format(curr_measurement, next_measurement))
    if (next_measurement > curr_measurement):
        print("increase")
        increase = increase +1 

print("increased measurements = {0}".format(increase))
