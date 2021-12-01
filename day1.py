
def problem1(): #dirty
    raw = open("data/day1.dat", "r")
    listFile = [int(x) for x in raw]
    previous = 0
    increase_count = -1

    for i in listFile:
        if i > previous:
            increase_count += 1
        previous = i

    print(increase_count)


def problem2():
    raw = open("data/day1.dat", "r")
    listFile = [int(x) for x in raw]
    previous = 0
    increase_count = -1

    resultList = []

    for i in range(0, len(listFile) - 2):
        temp = listFile[i] + listFile[i + 1] + listFile[i + 2]
        resultList.append(temp)

    for i in resultList:
        if i > previous:
            increase_count += 1
        previous = i

    print(increase_count)


def alt1(): #clean
    raw = open("data/day1.dat", "r")
    listFile = [int(x) for x in raw]

    returnList, returnAnswer = alt_call(listFile,'measurement')
    print(returnAnswer)


def alt2():
    raw = open("data/day1.dat", "r")
    listFile = [int(x) for x in raw]

    resultList = []
    for i in range(0, len(listFile) - 2):
        temp = listFile[i] + listFile[i + 1] + listFile[i + 2]
        resultList.append(temp)

    returnList, returnAnswer = alt_call(resultList,'sum')
    print(returnAnswer)


def alt_call(input, measureType):

    previous = input[0]
    results = [[previous, f'(N/A - no previous {measureType})']]

    for i in range(1,len(input)):
        if input[i] == previous:
            temp = [input[i], 'No change']
        elif input[i] < previous:
            temp = [input[i], 'Decrease']
        elif input[i] > previous:
            temp = [input[i], 'Increase']
        # print(temp)
        results.append(temp)
        previous = input[i]

    answer = sum(x.count('Increase') for x in results)
    return results, answer


problem1()
problem2()

alt1()
alt2()