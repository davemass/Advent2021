def problem1(file):
    fileRaw = [x for x in open(file, "r")]

    seven_segment_key = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

    for line in fileRaw:
        singleLine = line.split(' | ')
        keys = singleLine[0].split(' ')
        for k, v in enumerate(keys):
            keys[k] = ''.join(sorted(v))


        numbers = singleLine[1].split(' ')


#assert problem1("day8-test.dat") == 26

print(problem1("data/day8-test.dat"))
#print(problem1("day8.dat"))



# 2 sections = number 1
# 3 sections = number 7
# 4 sections = number 4
# 5 sections = numbers 2, 3, 5
# 6 sections = numbers 0, 6, 9
# 7 sections = number 8
