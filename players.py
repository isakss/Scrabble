#TODO: players class and board class

from LetterBag import LetterBag
from queue import Queue

class Player:
    def __init__(self, name, letters, score = 0):
        self.name = name
        self.score = score
        self.letter_list = letters
    
    def add_letters(self, letter_lis):
        for letter in letter_lis:
            self.letter_list.append(letter)
    
    def play_letters(self):
        letter_input = input("Enter the letter you want to play (Enter '1' to stop): ")

        while letter_input != "1":
            if letter_input not in self.letter_list:
                print("You do not have this letter on hand. Try another one!")
            else:
                index = self.letter_list.index(letter_input)
                letter = self.letter_list[index]
                #insert letter into board
                self.letter_list.remove(index)
            letter_input = input("Enter the letter you want to play (Enter '1' to stop): ")
        
    
    def swap_letters(self, amount):
        pass

    def get_letter(self, letter):
        return_val = None

        for i, letter_instance in enumerate(self.letter_list):
            if letter == letter_instance.key:
                return_val = self.letter_list.pop(i)
        
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

class TurnOrder:
    def __init__(self, capacity = 4):
        self.player_list = Queue(capacity)
    
    def insert_players(self, name, letters):
        self.player_list.put(Player(name, letters))
    
    def next_turn(self):
        returning_player = self.player_list.get_nowait()
        self.player_list.put(returning_player)

        return returning_player

"""
class PlayerNode:
    def __init__(self, data):
        self.next = None
        self.data = data

class PlayerList:
    def __init__(self, capacity = 4):
        self.head = None
        self.capacity = capacity
        self.current_node = self.head
        self.size = 0
    
    def insert(self, name):
        if self.size >= self.capacity:
            print("Sorry! Only a maximum of 4 players allowed!")
        else:
            new_player = PlayerNode(Player(name))
            tmp = self.head

            new_player.next = self.head
            self.current_node = new_player

            if self.head != None:
                while tmp.next != self.head:
                    tmp = tmp.next
                tmp.next = new_player
            else:
                new_player.next = new_player
        
            self.head = new_player
            self.size += 1
    
    def get_curr_pos(self):
        return self.current_node.data

    def move_to_next(self):
        self.current_node = self.current_node.next

    def __len__(self):
        return self.size

"""  
if __name__ == "__main__":
    pass


        
    

    