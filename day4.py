class BingoBoard():
    def __init__(self, r0, r1, r2, r3, r4):
        self.board = [r0, r1, r2, r3, r4]

    def numberPlayed(self, number_played):
        for i in range(5):
            for j in range(5):
                if self.board[i][j][0] == number_played:
                    self.board[i][j][1] = 1

    def checkWinner(self):
        for a in range(5):
            if self.board[a][0][1] == 1 and self.board[a][1][1] == 1 and self.board[a][2][1] == 1 and \
                    self.board[a][3][1] == 1 and self.board[a][4][1] == 1:
                return True
            if self.board[0][a][1] == 1 and self.board[1][a][1] == 1 and self.board[2][a][1] == 1 and \
                    self.board[3][a][1] == 1 and self.board[4][a][1] == 1:
                return True
        return False

    def sumUnmarkedNumbers(self, numberPlayed):
        result = 0
        for a in range(5):
            for b in range(5):
                if self.board[a][b][1] == 0: result += int(self.board[a][b][0])

        return result * numberPlayed


def createBoards(fileRaw):

    boards = []
    board_config = []
    for i in fileRaw:
        if len(i) > 1:
            numbers_split = i.split()
            numbers_split_status = []
            for j in numbers_split:
                numbers_split_status.append([j, 0])
            board_config.append(numbers_split_status)
            if len(board_config) == 5:
                a = BingoBoard(board_config[0], board_config[1], board_config[2], board_config[3], board_config[4])
                boards.append(a)
                board_config = []

    return boards

def problem1(file):
    fileRaw = [x for x in open(file, "r")]

    call_list = fileRaw.pop(0).split(',')
    fileRaw.pop(0)

    boards = createBoards(fileRaw)

    winning_number = -1
    for x in call_list:
        if winning_number != -1: break

        for y in boards:
            y.numberPlayed(x)

        for z in boards:
            if z.checkWinner() is True:
                winning_number = x
                winning_board = z

    result = winning_board.sumUnmarkedNumbers(int(winning_number))
    print(result)


def problem2(file):
    fileRaw = [x for x in open(file, "r")]

    call_list = fileRaw.pop(0).split(',')
    fileRaw.pop(0)

    boards = createBoards(fileRaw)

    keepSearching = True
    while keepSearching:
        x = call_list.pop(0)

        for y in boards[:]:
            y.numberPlayed(x)
            if y.checkWinner() is True:
                if len(boards) == 1:
                    result = y.sumUnmarkedNumbers(int(x))
                    keepSearching = False
                else:
                    boards.remove(y)



    print(result)


problem1("data/day4.dat")
problem2("data/day4.dat")


