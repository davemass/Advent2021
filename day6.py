class Fish:

    def __init__(self, timer=9):
        self.timer = int(timer)

    def age_by_a_day(self):
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            return 1


def problem1(file, number_days):
    fileRaw = [x for x in open(file, "r")]

    initial_fish = fileRaw[0].split(',')

    here_fishie_fishie = []

    for f in initial_fish:
        here_fishie_fishie.append(Fish(f))

    for d in range(number_days):
        for f in here_fishie_fishie:
            if f.age_by_a_day(): here_fishie_fishie.append(Fish())

    return len(here_fishie_fishie)


def problem2(file, number_days):
    with open(file, "r") as file:
        initial_fish = map(int, file.readline().split(','))

    fishie_fishies = [0] * 9

    for i in initial_fish:
        fishie_fishies[i] += 1

    for d in range(number_days):
        fishie_fishies = advanceOneDay(fishie_fishies)

    total = 0

    for f in fishie_fishies:
        total += f

    return total


def advanceOneDay(fishies):
    babies = fishies[0]

    for x in range(1, len(fishies)):
        fishies[x-1] = fishies[x]

    fishies[6] += babies
    fishies[8] = babies

    return fishies


assert problem1("data/day6-test.dat", 18) == 26
assert problem1("data/day6-test.dat", 80) == 5934

assert problem2("data/day6-test.dat", 18) == 26
assert problem2("data/day6-test.dat", 80) == 5934

print(problem1("data/day6.dat", 80))
print(problem2("data/day6.dat", 256))




