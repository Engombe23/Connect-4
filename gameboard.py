
class GameBoard:
    
    def __init__(self, num_rows=6, num_cols=7):
        self.__space = ' '
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__board =  []
            
        for i in range(self.__num_rows):
            row = [self.__space] * self.__num_cols
            self.__board.append(row)
    
    
    def get_num_rows(self):
        return self.__num_rows
    
    def get_num_cols(self):
        return self.__num_cols
    
    
    def is_board_full(self):
        row = ''
        for x in range(self.__num_rows):
            for y in range(self.__num_cols):
                row = self.__board[x][y]
                
            if row == self.__space:
                return False
            row = ''
        return True
        
    def is_space_free (self, row, col):
        if self.__board[row][col] == self.__space:
            return True
        return False
    
    def make_move(self, col, element):
        for i in range(self.__num_rows - 1, -1, -1):
            if self.is_space_free(i, col):
                self.__board[i][col] = element
                break

    def show_board_dynamic(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                print("| ", end="")
                print(self.__board[i][j], end=" ")
            print("|")
            self.__print_horizontal_line()
            print("")
    
    def __print_horizontal_line(self):
        print("+", end="")
        for i in range(self.__num_cols):
            end = "+"
            print("---", end=end)
        print("")
    
    
    def check_winner(self):
        # Return True if a player has 4 pieces in a row horizontally or vertically or diagonally
        return self.__check_winner_hz() or self.__check_winner_vt() or self.__check_winner_diag1() or self.__check_winner_diag2()
            
    
    def __check_winner_hz(self):
        for x in range(self.__num_rows):
            for y in range(self.__num_cols - 3): #3 is subtracted to avoid array out of bounds
                # For now have 'X' and 'O'
                if self.__board[x][y] == self.__board[x][y+1] == self.__board[x][y+2]== self.__board[x][y+3] and self.__board[x][y] in ['X','O']:
                    return True
        return False
    
    
    def __check_winner_vt(self):
        for y in range(self.__num_cols):
            for x in range(self.__num_rows - 3):
                if self.__board[x][y] == self.__board[x+1][y] == self.__board[x+2][y] == self.__board[x+3][y] and self.__board[x][y] in ['X', 'O']:
                    return True
        return False
    
    
    def __check_winner_diag1(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row
        # diagonally from left to right. This is required for the 50-59% marking criteria
        for x in range(self.__num_rows - 3):
            for y in range(self.__num_cols - 3):
                if self.__board[x][y] == self.__board[x+1][y+1] == self.__board[x+2][y+2] == self.__board[x+3][y+3] != ' ':
                    return True
        return False
    
    def __check_winner_diag2(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row
        # diagonally from right to left. This is required for the 50-59% marking criteria
        for y in range(self.__num_rows - 1, 2, -1):
            for x in range(self.__num_cols - 3):
                if self.__board[x][y] == self.__board[y-1][x+1] == self.__board[y-2][x+2] == self.__board[y-3][x+3] != ' ':
                    return True
        return False


        
        
        
        
        
        