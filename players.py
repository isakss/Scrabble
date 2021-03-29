from LetterBag import LetterBag
from queue import Queue

class Player: #Keeps track of the player name, score and his letters
    def __init__(self, name, letters, score = 0):
        self.name = name
        self.score = score
        self.letter_list = letters
    
    def add_letters(self, letter_lis):
        for letter in letter_lis:
            self.letter_list.append(letter)

    def get_letter(self, letter):
        return_val = None

        for i, letter_instance in enumerate(self.letter_list):
            if letter == letter_instance.key:
                return self.letter_list.pop(i)
        
        return return_val
    
    def display_letters(self):
        ret_str = ""
        for letter in self.letter_list:
            ret_str += str(letter) + " "
        
        return ret_str
    
    def display_score(self):
        return self.score
    
    def __str__(self):
        ret_str = ""

        ret_str += self.name + "\nScore: " + str(self.score) + "\nLetters on hand: " + str(self.letter_list) + "\n"

        return ret_str

class TurnOrder: #Keeps the players in a queue and returns the players and always adds them again at the back
    def __init__(self, capacity = 4):
        self.player_list = Queue(capacity)
    
    def insert_players(self, name, letters):
        self.player_list.put(Player(name, letters))
    
    def next_turn(self):
        returning_player = self.player_list.get_nowait()
        self.player_list.put(returning_player)

        return returning_player