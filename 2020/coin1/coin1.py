# take a value, then try with every other value




filename = "input"

with open(filename) as f:
    lines = f.read().splitlines()

# range(start,stop,step)
    
nums = []
print(len(lines))

incr = range(0, len(lines))

for pos in incr:
    #print(lines[pos])
    nums.append(int(lines[pos]))

sortedNums = sorted(nums)

print(sortedNums)
#quit()


for firstNum in sortedNums:
    for secondNum in sortedNums:
        if (firstNum + secondNum == 2020):
            print("got answer")
            print("nums = {} {}".format(firstNum, secondNum))
            answer = firstNum * secondNum
            print("result = {}".format(answer))
            quit()


def processList(sortedNums, numFromList, fromPos, endPos = len(sortedNums)-1):
    # get # entries in list 
    listLen = len(sortedNums)
    print("listPos = {}".format(endPos))
    listEntry = int(sortedNums[endPos])
    print("list entry = {}".format(listEntry))

    firstValue = int(sortedNums[fromPos])
    secondValue = int(sortedNums[endPos])

    calcVal = firstValue + secondValue

    # TODO tweak different arg, depending on value being too low or high.
    # only need one call to function in here

    # move to earlier part of list
    if calcVal == 2020:
        print("got required value")
        quit()
    elif calcVal < 2020: # move to later part of list
        print("value too low {} ".format(calcVal))
        print("firstPos = {}".format(fromPos))
        processList(sortedNums, firstValue, fromPos, endPos) 
    else:
        print("value too high {} ".format(calcVal))
        # divide listEntry by 2

        endPos = endPos//2
        print("endPos = {}".format(endPos))
        processList(sortedNums, numFromList, fromPos, endPos)





