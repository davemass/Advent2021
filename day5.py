def problem1(file):
    return linesAndFilters(file, 0)


def problem2(file):
    return linesAndFilters(file, 1)


def linesAndFilters(file, includeDiags):

    fileRaw = [x for x in open(file, "r")]
    coord_map = {}

    for fileLine in fileRaw:
        movement_string = fileLine.rstrip().replace(' -> ', ',')
        movement_split = movement_string.split(',')
        movement_int = list(map(int, movement_split))

        if (movement_int[0] == movement_int[2] or
            movement_int[1] == movement_int[3] or
            includeDiags):
            for traversal_item in Traversal(movement_int):
                coord_map[traversal_item] = coord_map.get(traversal_item, 0) + 1

    coord_values = coord_map.values()

    high_traffic_areas = 0
    for i in coord_values:
        if i > 1: high_traffic_areas += 1

    return high_traffic_areas


def Traversal(movement_int):

    result = []

    x_step = -1 if movement_int[0] > movement_int[2] else 1
    y_step = -1 if movement_int[1] > movement_int[3] else 1

    x_list = range(movement_int[0], movement_int[2] + x_step, x_step)
    y_list = range(movement_int[1], movement_int[3] + y_step, y_step)

    max_fill = max(len(x_list), len(y_list))

    if len(x_list) < max_fill: x_list = [x_list[0]] * max_fill
    if len(y_list) < max_fill: y_list = [y_list[0]] * max_fill

    for build_line in range(max_fill):
        result.append(f'{x_list[build_line]},{y_list[build_line]}')

    return result


assert Traversal([3, 10, 3, 12]) == ['3,10', '3,11', '3,12']                    #Static X, Incr Y
assert Traversal([4, 9, 7, 9]) == ['4,9', '5,9', '6,9', '7,9']                  #Static Y, Incr X
assert Traversal([5, 6, 5, 2]) == ['5,6', '5,5', '5,4', '5,3', '5,2']           #Static X, Decr Y
assert Traversal([9, 6, 4, 6]) == ['9,6', '8,6', '7,6', '6,6', '5,6', '4,6']    #Static Y, Decr X

assert Traversal([1, 5, 4, 8]) == ['1,5', '2,6', '3,7', '4,8']                  #Diag UR to LL
assert Traversal([8, 3, 6, 1]) == ['8,3', '7,2', '6,1']                         #Diag UL to LR
assert Traversal([2, 6, 5, 3]) == ['2,6', '3,5', '4,4', '5,3']                  #Diag LL to UP
assert Traversal([8, 9, 5, 6]) == ['8,9', '7,8', '6,7', '5,6']                  #Diag LR to UL

assert problem1("data/day5-test.dat") == 5
assert problem1("data/day5.dat") == 6666

assert problem2("data/day5-test.dat") == 12
assert problem2("data/day5.dat") == 19081

print(problem1("data/day5.dat"))
print(problem2("data/day5.dat"))

