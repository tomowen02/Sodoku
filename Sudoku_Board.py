class Sudoku_Board:
    def __init__(self):
        self.board = [
            [0,0,0,0,0,0,0,0,0], # Bottom row
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0] # Top row
        ]
    
    def print_board(self):
        print(f'''
        {self.__print_row(self.board[0])}
        {self.__print_row(self.board[1])}
        {self.__print_row(self.board[2])}
        ------+-------+------
        {self.__print_row(self.board[3])}
        {self.__print_row(self.board[4])}
        {self.__print_row(self.board[5])}
        ------+-------+------
        {self.__print_row(self.board[6])}
        {self.__print_row(self.board[7])}
        {self.__print_row(self.board[8])}
        ''')

    def __print_row(self, row):
        output = ''
        
        for i in range(0,3):
            output += self.__display_digit(row[i]) + ' '
        output += '| '
        for i in range(3,6):
            output += self.__display_digit(row[i]) + ' '
        output += '| '
        for i in range(6,9):
            output += self.__display_digit(row[i]) + ' '

        return output

    def __display_digit(self, digit):
        if digit == 0:
            return ' '
        else:
            return str(digit)