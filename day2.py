
def problem1():
    raw = open("data/day2.dat", "r")

    splitList = [x.split() for x in raw]
    intList = [[x[0], int(x[1])] for x in splitList]

    movement = {"forward": 0, "down": 0, "up": 0}

    for x in intList:
        newValue = movement.get(x[0]) + x[1]
        updatedDic = {x[0]: newValue}
        movement.update(updatedDic)

    answer = movement.get("forward") * (movement.get("down") - movement.get("up"))
    print(answer)


def problem2():
    raw = open("data/day2.dat", "r")
    movement = {"forward" : 0, "depth": 0, "aim" : 0}
    splitList = [x.split() for x in raw]
    intList = [[a[0], int(a[1])] for a in splitList]

    for x in intList:
        if x[0] == "forward":
            newForwardDic = {"forward": movement.get("forward") + x[1]}
            movement.update(newForwardDic)
            newDepthDic = {"depth": movement.get("depth") + (movement.get("aim") * x[1])}
            movement.update(newDepthDic)
        else:
            up_down = x[1] if x[0] == "down" else -x[1]
            newAimValue = movement.get("aim") + up_down
            newAimDic = {"aim": newAimValue}
            movement.update(newAimDic)

    answer = movement.get("forward") * movement.get("depth")
    print(answer)


problem1()
problem2()