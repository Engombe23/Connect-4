# -*- coding: utf-8 -*-
"""
Created on 12th Feb 2024

@author: Engombe Lokanga & Mohamed Cisman
"""

from gameboard import GameBoard
from player import HumanPlayer, ComputerPlayer
from gamegui import GameGUI



def main():
    
    gboard = GameBoard()
    # create player 1 object
    p1 = HumanPlayer("X", gboard)
    # TODO: create player 2 object
    p2 = ComputerPlayer("O", gboard)
    
    # TODO: Place players 1 and 2 in tuple for turn based game. 
    players_lst = (p1, p2)
    
    winner = False
    
    # show empty grid at the beginning of the game
    gboard.show_board_dynamic()
    
    while (winner == False):
        # This is to allow players to take turns. 
        # The game begins with the player at index zero in the tuple,
        # When the player completes its turn, the next player in the tuple will be asked to play. 
        # If there is no winner, this will continue until reaching the end of the players list, 
        # and then we start again from the beggining of the list.
        
        for p in players_lst:
            p.play()
            # After each move, the board is shown on the screen
            gboard.show_board_dynamic()
            
            # TODO: Use the check_winner() method of the GameBoard class to check
            # if a player has won the game
            winner = gboard.check_winner()
            
            if winner == True:
                # Show current player's symbol as Winner,
                # and terminate the game (DONE)
                print("Player %s is the Winner!" % p.get_player_symbol())
                return
                
            # TODO: Add an if statement to check if the board is full. If the board
            # is full, print a message and end the game (DONE)
            board_is_full = gboard.is_board_full()
            
            if board_is_full:
                print("The board is full, the game ends a draw!")
                exit()
                            

if __name__ == "__main__":
    print("Welcome to Connect4!")
    while True:
        print("Choose interface:")
        print("\t 1. Console")
        print("\t 2. GUI")
        choice = input("Enter number to choose interface or q to quit: ")
        if choice.lower() == "q":
            break
        if choice == "1":
            print("")
            main()
        elif choice == "2":
            b_gui = GameGUI()
            b_gui.initialise()
            break
