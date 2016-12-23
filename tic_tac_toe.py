from tic_tac_toe_graphics import *


def BoardClicked(col_index, row_index):
        global player
        global symbol
        global endgame
        
        if board_values[col_index][row_index] == None and endgame == False:
                print('BoardClicked col_index:', col_index, 'row_index:', row_index)
                board.mark_square(col_index, row_index, symbol)
                board_values[col_index][row_index] = symbol 
                PrintBoardValues()
                player +=1
                
        if player % 2 == 0:
                symbol = 'x'
                print(board.display_message('Player X turn'))
        else:
                symbol = 'o'
                print(board.display_message('Player O turn'))
                                            
        if CheckWinner('x') == True:
                print(board.display_message('Player X is the winner'))
                      
        elif CheckWinner('o')== True:
                print(board.display_message('Player O is the winner'))
                      
        elif player == 9:
                print(board.display_message('The game is a draw'))
                
                        
def PrintBoardValues():
        for row in range(3):
                print(board_values[row])
                
def CheckWinner(symbol):
        global endgame
        if symbol == board_values[0][0] and symbol == board_values[1][0] and symbol == board_values[2][0]:
                endgame = True
                return True
        elif symbol == board_values[0][1] and symbol == board_values[1][1] and symbol == board_values[2][1]:
                endgame = True
                return True
        elif symbol == board_values[0][2] and symbol == board_values[1][2] and symbol == board_values[2][2]:
                endgame = True
                return True
        elif symbol == board_values[0][0] and symbol == board_values[0][1] and symbol == board_values[0][2]:
                endgame = True
                return True
        elif symbol == board_values[1][0] and symbol == board_values[1][1] and symbol == board_values[1][2]:
                endgame = True
                return True
        elif symbol == board_values[2][0] and symbol == board_values[2][1] and symbol == board_values[2][2]:
                endgame = True
                return True
        elif symbol == board_values[0][0] and symbol == board_values[1][1] and symbol == board_values[2][2]:
                endgame = True
                return True
        elif symbol == board_values[2][0] and symbol == board_values[1][1] and symbol == board_values[0][2]:
                endgame = True
                return True

board = TicTacToeBoard(3, 3, BoardClicked) 
board_values = [[None, None, None],
                [None, None, None],
                [None, None, None]]

player = 0
symbol = 'x'
endgame = False
# Make sure mainloop() is the last line of code in this program!
mainloop()
