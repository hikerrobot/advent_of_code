# take a value, then try with every other value

# sorting?
# divide and conquer?
# most efficient method


filename = "input"

with open(filename) as f:
    lines = f.read().splitlines()

# range(start,stop,step)
    
nums = []
print(len(lines))
print(len(nums))

incr = range(0, len(lines))
print(incr)

for pos in incr:
    #print(lines[pos])
    nums.append(int(lines[pos]))

sortedNums = sorted(nums)

print(sortedNums)

#quit()


def processList(sortedNums, firstPos = 0, endPos = len(sortedNums)-1):
    # get # entries in list 
    listLen = len(sortedNums)
    print("listPos = {}".format(endPos))
    listEntry = int(sortedNums[endPos])
    print("list entry = {}".format(listEntry))

    firstValue = int(sortedNums[firstPos])
    secondValue = int(sortedNums[endPos])

    print(type(firstValue))

    calcVal = firstValue + secondValue
    print(type(calcVal))

    # TODO tweak different arg, depending on value being too low or high.
    # only need one call to function in here

    # move to earlier part of list
    if calcVal > 2020:
        print("value too high {} ".format(calcVal))
        # divide listEntry by 2

        endPos = endPos//2
        print("endPos = {}".format(endPos))
        #processList(sortedLines, firstPos, listPos // 2)
    else: # move to later part of list
        print("value too low {} ".format(calcVal))
        firstPos = endPos//2
        print("firstPos = {}".format(firstPos))
        #processList(sortedLines, firstValue, newListPos) 
        
    #processList(sortedLines, firstPos, endPos)


processList(sortedNums)

