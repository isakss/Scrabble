from operations import Operations
"""
from players import TurnOrder
from LetterBag import LetterBag
from board import Board
"""
def choose_letters(player_instance):
    letter_input = ""
    returning_list = []

    while letter_input != "1":
        letter_input = input("Choose a letter to use for this action (Enter 1 to stop picking letters): ").capitalize()
        letter_instance = player_instance.get_letter(letter_input)

        if letter_instance == None and letter_input != "1":
            print("You do not have this letter on hand!")
        elif letter_input == "1" and returning_list == []:
            return None
        elif letter_input == "1":
            continue
        else:
            returning_list.append(letter_instance)

    return returning_list

def order_list(letter_list):
    returning_list = []
    print("Here are your letters: {}".format(letter_list))
    print("Choose the letters in the order you want the word to be written")
    for letter in letter_list:
        new_letter = input("Next letter: ").capitalize()
        for letter2 in letter_list:
            if new_letter == letter2.key:
                returning_list.append(letter2)
                continue

    return returning_list

if __name__ == "__main__":
    print("--Welcome to Scrabble!--")
    player_amount = 0
    operations = Operations()

    while player_amount < 2 or player_amount > 4:
        player_amount = input("Choose how many are playing (2-4 players) or enter 1 to quit: ")

        try:
            player_amount = int(player_amount)
        except ValueError():
            print("You have to enter a number!")
            player_amount = 5
        
        if player_amount == 1:
            quit()
    
    player_lis = []

    for i in range(1, player_amount + 1):
        player_input = input("Enter name for player {}: ".format(i))
        player_lis.append(player_input)
    
    operations.setup(player_lis)
    
    while True:
        current_player = operations.get_next_turn()
        operations.print_board()
        print("\nPlayer {}, its your turn!\n".format(current_player.name))
        print("These are your letters:\n{}".format(current_player.display_letters()))

        option_input = "4"

        while option_input not in "123":
            print("These are your actions:\n1. Play letters\n2. Swap out letters\n3. Skip turn")
            option_input = input("Choose your action this turn: ")

    
            if option_input == "1":
                correct_pos = False
                while correct_pos == False:
                    row_input = int(input("Enter the row you wish to insert into: "))
                    column_input = int(input("Enter the column you wish to insert into: "))
                    correct_pos = operations.get_value_at_pos(row_input, column_input)
                    if correct_pos == False:
                        print("Invalid position")

                direction = ""
                while direction != "V" and direction != "H":
                    direction = input("Enter the direction (V for vertical and H for horizontal): ").capitalize()

                letter_list = choose_letters(current_player)
                if letter_list == None:
                    option_input = ""
                else:
                    if correct_pos != "\u2605":
                        letter_list.append(correct_pos)

                    new_list = order_list(letter_list)
                    for i, letter in enumerate(new_list):
                        if correct_pos != "\u2605" and letter.key == correct_pos.key:
                            if direction == "H":
                                column_input = column_input - i
                            else:
                                row_input = row_input - i
                    the_point = operations.play_letters(new_list, row_input, column_input, direction)
            elif option_input == "2":
                letter_list = choose_letters(current_player)
                if letter_list == None:
                    option_input = ""
                else:
                    operations.swap_letters(letter_list, current_player)
            else:
                continue

        input()








    