class Player:
    
    def __init__(self, symbol, board):
        self.__symbol = symbol
        self._gboard = board
        
    def get_player_symbol(self):
        return self.__symbol
    

class HumanPlayer(Player):
    
    def __init__(self, symbol, board):
        Player.__init__(self, symbol, board)
    
    def play(self):
        # This method defines mechanism for the human players to play.
        # TODO: Get input from the player about the column in which they wish to place their mark.
        # Check if the input is valid and then place the player's symbol in that column = make_move(col, element),
        # if the column is not full (DONE)
        print("Player %s turn" %self.get_player_symbol())
        while (True):
            try:
                col = int(input("Please enter column no : "))
                if col < 1 and col >= self._gboard.get_num_cols():
                    print("Invalid column number. Please enter a number between 0 and %d" % (self._gboard.get_num_cols() - 1))
                    continue
                elif self._gboard.is_space_free(0, col):
                    symbol = self.get_player_symbol()
                    self._gboard.make_move(col, symbol)
                    break 
                else:
                    print("Column is full. Please choose another column.")
            except ValueError:
                print("Inavlid input. Please enter valid column number")
                    

import random

class ComputerPlayer(Player):
    
    def __init__(self, symbol, board, buttons_2d_list = []):
        Player.__init__(self, symbol, board)
        self.buttons_2d_list = buttons_2d_list
    
    def play(self):
        # If the computer player is created for the GUI game, it needs to use the
        # GUI's button list (therefore, buttons_2d_list will not be empty). In that
        # case, the __play_gui() method will be called. See __play_gui() method for info
        if len(self.buttons_2d_list) > 0:
            self.__play_gui()
            return
        print("Player %s turn" %self.get_player_symbol())
        # TODO: Generate a random number for the column and then use the make_move()
        # method to place the player's symbol in that column, if the column is not full (DONE)
        while True:
            col = random.randint(0, self._gboard.get_num_cols()-1)
            if self._gboard.is_space_free(0, col):
            
                symbol = self.get_player_symbol()
                self._gboard.make_move(col, symbol)
                break
        
            
    
    def __play_gui(self):
        # This method is to be used when the computer player is created for the GUI game.
        # TODO: Generate a random number for the column and then use the buttons_2d_list
        # to invoke() a click on the appropriate button of that column (DONE)
        while True:
            col = random.randint(0, self._gboard.get_num_cols() - 1)
            if self._gboard.is_space_free(0, col):
                self._gboard.make_move(col, self.get_player_symbol())
            return col 