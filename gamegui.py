import tkinter
from sys import exit
from tkinter import messagebox, simpledialog
from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer
from functools import partial

class GameGUI:
    
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.title("Connect Four")
        
        self.menu = tkinter.Menu(self.mw)
        self.mw.config(menu=self.menu)
        
        self.file_menu = tkinter.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File")
        
        self.menu.add_command(label="Restart", command=self.restart_game)         
        self.menu.add_command(label="Quit", command=self.quit_game)
        
        self.colors = {"X": "red", "O": "yellow"}  # Default colors
        
    def restart_game(self):         
        self.mw.destroy()         
        main()     
        
    def quit_game(self):         
        self.mw.destroy()

    def clicked_btn(self, x, y):
        p = self.players_lst[self.current_player_index]
        
        button = self.buttons_2d_list[x][y]
        if button["text"] == " ":
            symbol = p.get_player_symbol()
            color = self.colors[symbol]
            
            button["text"] = symbol
            button.config(bg=color)
            
            self.gboard.make_move(y, symbol)
            winner = self.gboard.check_winner()
            if winner:
                win_message = "Player %s is the Winner!" % symbol
                messagebox.showinfo("Winner Info", win_message)
                self.mw.destroy()
                exit()
            
            board_is_full = self.gboard.is_board_full()
            if board_is_full:
                messagebox.showinfo("Game Info", "The board is full, the game ends in a draw!")
                self.mw.destroy()
                exit()
            
            self.current_player_index += 1
            if self.current_player_index >= len(self.players_lst):
                self.current_player_index = 0
            
            current_player = self.players_lst[self.current_player_index]
            if isinstance(current_player, ComputerPlayer):
                current_player.play()
    
    def update_button_text(self, col, element):
        for row in range(self.gboard.get_num_rows() - 1, -1, -1):
            button = self.buttons_2d_list[row][col]
            if button["text"] == " ":
                button["text"] = element
                color = self.colors[element]
                button.config(bg=color)
                button.config(state="disabled")
                break
                
    def __initialise_game(self, gboard, players_lst, current_player_index=0):
        self.gboard = gboard
        self.players_lst = players_lst
        self.current_player_index = current_player_index
        
        self.winner = False
        
        self.buttons_2d_list = []
        for x in range(self.gboard.get_num_rows()):
            row = []
            for y in range(self.gboard.get_num_cols()):
                self.button = tkinter.Button(self.mw, text=" ", font=('Arial 10 bold'), height=5, width=10)
                self.button.config(command=partial(self.clicked_btn, x, y))
                self.button.grid(row=x, column=y)
                row.append(self.button)
            self.buttons_2d_list.append(row)
               
        current_player = self.players_lst[self.current_player_index]
        if isinstance(current_player, ComputerPlayer):
            current_player.play()
    
    def initialise(self):
        gboard = GameBoard()
        self.buttons_2d_list =  []
        for i in range(gboard.get_num_rows()):
            self.row = [' '] * gboard.get_num_cols()
            self.buttons_2d_list.append(self.row)
        
        p1 = ComputerPlayer("O", gboard, self.buttons_2d_list)
        p2 = HumanPlayer("X", gboard)
        
        players_lst = (p2, p1)
        
        # Color selection dialog
        p1_color = simpledialog.askstring("Player 1 Color", "Choose color for Player 1 (X):")
        p2_color = simpledialog.askstring("Player 2 Color", "Choose color for Player 2 (O):")
        
        if p1_color:
            self.colors["X"] = p1_color
        if p2_color:
            self.colors["O"] = p2_color
        
        self.__initialise_game(gboard, players_lst)
        
        tkinter.mainloop()
                

def main():
    b_gui = GameGUI()
    b_gui.initialise()
        
if __name__ == "__main__":
    main()