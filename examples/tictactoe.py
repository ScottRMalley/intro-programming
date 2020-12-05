
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class TicTackGame:
    def __init__(self):
        self.board = [i for i in range(0, 9)]
        self.current_player = 'X'
        self.x_wins = False
        self.o_wins = False

    def start_game(self):
        while True:
            self.print_board()
            self.check_wins()
            if self.x_wins:
                print('X wins!')
                return
            if self.o_wins:
                print('O wins')
                return
            if self.is_complete():
                print('It was a tie!')
                return
            next_move = int(input('place {} in space:'.format(self.current_player)))
            self.board[next_move] = self.current_player

            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    def print_board(self):
        colored_board_string = []
        for player in self.board:
            if player == 'X':
                colored_board_string.append('{}{}{}'.format(bcolors.WARNING, player, bcolors.ENDC))
            elif player == 'O':
                colored_board_string.append('{}{}{}'.format(bcolors.OKBLUE, player, bcolors.ENDC))
            else:
                colored_board_string.append(player)
        board_string = '| {} | {} | {} |\n| {} | {} | {} |\n| {} | {} | {} |\n'\
            .format(*colored_board_string)
        print(board_string)

    def check_wins(self):
        # first check rows
        for i in range(3):
            current_row = self.board[i*3: (i+1)*3]
            if current_row == ['X', 'X', 'X']:
                self.x_wins = True
                return
            if current_row == ['O', 'O', 'O']:
                self.o_wins = True
                return

        # then check columns
        for i in range(3):
            current_column = [self.board[i], self.board[i+3], self.board[i+6]]
            if current_column == ['X', 'X', 'X']:
                self.x_wins = True
                return
            if current_column == ['O', 'O', 'O']:
                self.o_wins = True
                return

        # then check diagonals
        diagonals = [[self.board[0], self.board[4], self.board[8]],
                     [self.board[2], self.board[4], self.board[6]]]
        for diagonal in diagonals:
            if diagonal == ['X', 'X', 'X']:
                self.x_wins = True
                return
            if diagonal == ['O', 'O', 'O']:
                self.o_wins = True
                return

    def is_complete(self):
        for item in self.board:
            if item != 'O' and item != 'X':
                return False
        return True


if __name__ == '__main__':
    tictac = TicTackGame()
    while input('Start a new game? ') == 'yes':
        tictac.start_game()
