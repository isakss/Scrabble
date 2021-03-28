from LetterBag import LetterBag
from players import TurnOrder
from board import Board

class Operations:
    def __init__(self):
        self.letter_bag = LetterBag()
        self.turn_order = TurnOrder()
        self.game_board = Board()
    
    def setup(self, player_list):
        for p in player_list:
            letters = self.letter_bag.draw_letters(7)
            self.turn_order.insert_players(p, letters)
    
    def get_next_turn(self):
        return self.turn_order.next_turn()
    
    def swap_letters(self, letter_list, curr_player):
        new_letters = self.letter_bag.swap_letters(letter_list)
        curr_player.add_letters(new_letters)

    def get_value_at_pos(self, row, col):
        return self.game_board.get_value_at_pos(row, col)

    def play_letters(self, letter_list, row, col, direction):
        self.game_board.add_word(letter_list, row, col, direction)

    def print_board(self):
        print(self.game_board)
