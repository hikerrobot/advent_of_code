import fileinput

filename = "1.input"

with open(filename) as f:
    lines = f.read().splitlines()

# print(type(lines))

tup = tuple(lines)
# print(type(tup))

increase = 0
processed = 0

print(len(tup))
for measure in range(0, len(tup)-1):
    processed=processed+1

    print("current: {0}, next {1}".format(tup[measure], tup[measure+1]))
    if (measure == 0):
        print("{0} - first measurement".format(tup[measure]))

    if (tup[measure] < tup[measure+1]):
        print("**increase")
        increase=increase+1
    else:
            print("decrease")


    # if (processed == 10):
    #     break
# track is previous measurement was greater than current measurement
# and not including first measurement

# don't want to compare until have 2 measurements


print("increased measurements: {0}".format(increase))
print("processed = {0}".format(processed))

    
