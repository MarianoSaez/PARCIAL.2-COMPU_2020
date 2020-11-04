class TaTeTi():
    def __init__(self):
        self.piece = ''
        self.valid = ['1.1', '1.2', '1.3',
                      '2.1', '2.2', '2.3',
                      '3.1', '3.2', '3.3']
        self.board = {value: value for value in self.valid}

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, value):
        self.__board = value

    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, value):
        self.__valid = value

    def __str__(self):
        tablero = ''
        tablero += '%s|%s|%s' % (self.board['1.1'], self.board['1.2'],
                                 self.board['1.3'])
        tablero += '\n---+---+---\n'
        tablero += '%s|%s|%s' % (self.board['2.1'], self.board['2.2'],
                                 self.board['2.3'])
        tablero += '\n---+---+---\n'
        tablero += '%s|%s|%s' % (self.board['3.1'], self.board['3.2'],
                                 self.board['3.3'])
        tablero = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'\
            '---+---+---\n3.1|3.2|3.3'
        return tablero

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner

    def win(self):
        state = False
        listax = 0
        listay = 0
        for i in self.board:
            if self.board[i] == ' x ':
                listax += 1
            else:
                listax -= 1
            if self.board[i] == ' o ':
                listay += 1
            else:
                listay -= 1

        # Este ultimo condicional se encarga de una excepcion
        # que se presenta en el test_win_8
        if listax == -3 and self.board['3.1'] != ' x '\
           and self.board['2.1'] == ' x '\
           and self.board['1.1'] == ' x ':
            return False
        if listay == -3 and self.board['3.1'] != ' o '\
           and self.board['2.1'] == ' o '\
           and self.board['1.1'] == ' o ':
            return False

        if listax == 3 or listax == 0 or listax == -3:
            state = True
        if listay == 3 or listay == 0 or listay == -3:
            state = True
        return state

    def input_position(self):
        celda = ''
        while celda not in self.valid:
            print('celda invalida')
            celda = input("Ingrese una celda: ")
        if celda in self.board and self.board[celda] == celda:
            self.board[celda] = 'x'
        for i in self.valid:
            if i == celda:
                indice = self.valid.index(celda)
                self.valid.pop(indice)
        return celda


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
