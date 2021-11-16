#author: Patryk Dąbkowski
game = 0
class board:
    a1 = " "
    a2 = " "
    a3 = " "
    b1 = " "
    b2 = " "
    b3 = " "
    c1 = " "
    c2 = " "
    c3 = " "
    winer = 0
    def __init__(self):
        print('\n', 'Round:')
        print(" ", "|", '1', "|", '2', "|", '3', "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('a', "|", self.a1, "|", self.a2, "|", self.a3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('b', "|", self.b1, "|", self.b2, "|", self.b3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('c', "|", self.c1, "|", self.c2, "|", self.c3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
    def print(self):
        print('\n', 'Round:')
        print(" ", "|", '1', "|", '2', "|", '3', "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('a', "|", self.a1, "|", self.a2, "|", self.a3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('b', "|", self.b1, "|", self.b2, "|", self.b3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
        print('c', "|", self.c1, "|", self.c2, "|", self.c3, "|")
        print("-", "-", "-", "-", "-", "-", "-", "-")
    def checker(self):
        if (self.a1 == self.a2 == self.a3 and self.a1 != ' '):
            print('\n', self.a1, "Win!", '\n')
            self.winer = 1
        elif (self.b1 == self.b2 == self.b3 and self.b1 != ' '):
            print('\n', self.b1, "Win!", '\n')
            self.winer = 1
        elif (self.c1 == self.c2 == self.c3 and self.c1 != ' '):
            print('\n', self.c1, "Win!", '\n')
            self.winer = 1
        elif (self.a1 == self.b1 == self.c1 and self.a1 != ' '):
            print('\n', self.a1, "Win!", '\n')
            self.winer = 1
        elif (self.a2 == self.b2 == self.c2 and self.a2 != ' '):
            print('\n', self.a2, "Win!", '\n')
            self.winer = 1
        elif (self.a3 == self.b3 == self.c3 and self.a3 != ' '):
            print('\n', self.a3, "Win!", '\n')
            self.winer = 1
        else:
            print("Next Round")
    def move(self, field, user):
        if field == 'a1':
            self.a1 = user
        elif field == 'a2':
            self.a2 = user
        elif field == 'a3':
            self.a3 = user
        elif field == 'b1':
            self.b1 = user
        elif field == 'b2':
            self.b2 = user
        elif field == 'b3':
            self.b3 = user
        elif field == 'c1':
            self.c1 = user
        elif field == 'c2':
            self.c2 = user
        elif field == 'c3':
            self.c3 = user
def play(game):
    game = game + 1
    user = ' '
    while board.winer == 0:
        if user == 'x':
            user = 'o'
        elif user == 'o':
            user = 'x'
        else:
            user = input('Chose first player: ')
        board.print()
        print(user)
        field = input('Chose your field: ')
        board.move(field, user)
        board.checker()
while 1:
    board = board()
    if game == 0:
        play(game)
    else:
        answer = input('Do you want to play in your ', game, 'game?')
        if answer == 'yes':
            play(game)
        elif answer == 'no':
            break
        else:
            print('Valid Answer')
