def problem1(file):
    with open(file, "r") as file:
        crabs = list(map(int, file.readline().split(',')))

    h_value = max(crabs)
    l_value = min(crabs)

    result_dict = {}

    for i in range(l_value, h_value):
        fuel = 0
        for x in crabs:
            fuel += abs(x-i)
        result_dict[i] = fuel

    min_fuels = min(result_dict.values())
    return min_fuels


def problem2(file):
    with open(file, "r") as file:
        crabs = list(map(int, file.readline().split(',')))

    h_value = max(crabs)
    l_value = min(crabs)

    cost = distanceCost(h_value - l_value)
    result_dict = {}

    for i in range(l_value, h_value):
        fuel = 0
        for x in crabs:
            fuel += cost.get(abs(x-i))
        result_dict[i] = fuel

    min_fuels = min(result_dict.values())
    return min_fuels


def distanceCost(value):
    result = {0:0}
    for i in range(1, value + 1):
        result[i] = max(result.values()) + i
    return result


assert problem1("data/day7-test.dat") == 37
assert problem2("data/day7-test.dat") == 168

print(problem1("data/day7.dat"))
print(problem2("data/day7.dat"))