
def problem1():
    listRaw = [x for x in open("data/day3.dat", "r")]

    currentCount = [0 for x in range(len(listRaw[0]) - 1)]
    for i in listRaw:
        for j in range(len(i)):
            if i[j] == "1":
                currentCount[j] += 1

    gammaStr = ""
    for i in currentCount:
        gammaStr += "1" if i / len(listRaw) >= 0.5 else "0"

    deltaStr = "1" * len(gammaStr)

    gamma = int(gammaStr, 2)
    delta = int(deltaStr, 2)

    epsilon = int(bin(gamma ^ delta), 2)

    print(gamma * epsilon)


def problem2():
    listRaw = [x for x in open("data/day3.dat", "r")]

    oxy = listRaw[:]
    co2 = listRaw[:]

    for i in range(len(listRaw[0]) - 1):
        if len(oxy) > 1:
            x = findMostCommon(oxy, i)
            oxy = list(filter(lambda a: a[i] == str(abs(x)), oxy))

        if len(co2) > 1:
            y = findMostCommon(co2, i)
            co2 = list(filter(lambda b: b[i] == str(abs(abs(y) - 1)), co2))


    int_oxy = int(oxy[0], 2)
    int_co2 = int(co2[0], 2)

    print(int_co2 * int_oxy)



def findMostCommon(list_of_values, position_to_evaluate):
    result_count = [0, 0]

    for x in list_of_values:
        if x[position_to_evaluate] == '0':
            result_count[0] += 1
        else:
            result_count[1] += 1

    result = -1
    if result_count[0] > result_count[1]: result = 0
    if result_count[1] > result_count[0]: result = 1

    return result


problem1()
problem2()



