# take a value, then try with every other value

filename = "input"

with open(filename) as f:
    lines = f.read().splitlines()

# range(start,stop,step)
    
nums = []
# print(len(lines))

incr = range(0, len(lines))

for pos in incr:
    #print(lines[pos])
    nums.append(int(lines[pos]))

sortedNums = sorted(nums)

# print(sortedNums)


def findValues(sortedNums):
    for firstNum in sortedNums:
        for secondNum in sortedNums:
            if (firstNum + secondNum == 2020):
                print("got answer")
                print("nums = {} {}".format(firstNum, secondNum))
                answer = firstNum * secondNum
                print("result = {}".format(answer))
                return


# with sorted values, obtain the middle value
# determine which half of list is needed based on sum
# split list in half, repeat

def processList(num, numberList):
    print("-------------------------------------------------")

    splitPoint = len(numberList) // 2;
    # print("splitPoint {}".format(splitPoint))

    secondNumber = numberList[splitPoint]

    print("nums = {}:{}".format(num, secondNumber))

    # print("list length = {}".format(len(numberList)))
    if len(numberList) == 1:
        # print("return - only 1 number")
        return

    print("sum = {}".format(num+secondNumber))

    if num + secondNumber > 2020:
        newList = numberList[0:splitPoint]
    elif num + secondNumber < 2020:
        newList = numberList[splitPoint:len(numberList)]
    else:
        print("*** huzzah! a match")
        quit()

    print(newList)
    print("new array length {}".format(len(newList)))
    processList(num, newList)

numsProcessed = 1

for num in sortedNums:
    print ("processing number {} : {}".format(numsProcessed, num))
    processList(num, sortedNums)
    numsProcessed=+1








