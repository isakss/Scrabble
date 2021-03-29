from LetterBag import LetterBag
from players import TurnOrder
from board import Board
from WordChecker import WordChecker

class Operations:
    def __init__(self):
        self.letter_bag = LetterBag()
        self.turn_order = TurnOrder()
        self.game_board = Board()
        self.word_checker = WordChecker()
    
    def setup(self, player_list):
        """Draws letters for all the players and puts them in a queue for the turn order"""
        for p in player_list:
            letters = self.letter_bag.draw_letters(7)
            self.turn_order.insert_players(p, letters)
    
    def get_next_turn(self):
        """Returns the next player in the turn order"""
        return self.turn_order.next_turn()
    
    def swap_letters(self, letter_list, curr_player):
        """Gives the letter bag the letters and expects new letters then adds them to the player"""
        new_letters = self.letter_bag.swap_letters(letter_list)
        curr_player.add_letters(new_letters)

    def get_value_at_pos(self, row, col):
        """Asks the game board for the letter at certain position if no letter then it gets false back"""
        return self.game_board.get_value_at_pos(row, col)

    def play_letters(self, letter_list, row, col, direction):
        """Gives game board what it needs to write the word and expects to get the point value for that word back"""
        return self.game_board.add_word(letter_list, row, col, direction)

    def print_board(self):
        print(self.game_board)

    def draw_letters(self, amount, current_player):
        new_letters = self.letter_bag.draw_letters(amount)
        current_player.add_letters(new_letters)

    def empty_check(self):
        return self.letter_bag.empty

    def check_word(self, letter_list):
        """Tries to get the value with certain key if KeyError then it is an invalid word and returns false else it returns true"""
        string_check = ""
        for letter in letter_list:
            string_check += str(letter)

        try:
            self.word_checker.dict[string_check]
            return True
        except KeyError:
            return False

    def return_letters_to_hand(self, letter_list, current_player):
        current_player.add_letters(letter_list)