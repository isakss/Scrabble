from operations import Operations

def choose_letters(player_instance):
    """Function that allows the player to choose which letters he/she wants to use just needs to press 1 to stop selecting"""
    letter_input = ""
    returning_list = []

    while letter_input != "1":
        letter_input = input("Choose a letter to use for this action (Enter 1 to stop picking letters): ").capitalize()
        letter_instance = player_instance.get_letter(letter_input)

        if letter_instance == None and letter_input != "1": #If player picks a letter that he does not own
            print("You do not have this letter on hand!")
        elif letter_input == "1" and returning_list == []: #If player wants to cancel and do something else
            return None
        elif letter_input == "1": # Make him skip the else if he picks the 1
            continue
        else:
            returning_list.append(letter_instance)

    return returning_list

def order_list(letter_list):
    """Function that allows players to order the letters to make the word with the one on the board unless it is empty"""
    returning_list = []
    print("Here are your letters:", end=" ")

    for letter in letter_list:
        print(letter, end=" ")

    print("\nChoose the letters in the order you want the word to be written")
    while len(letter_list) > 0: # End when the player has placed all his letters
        new_letter = input("Next letter: ").capitalize()
        for i, letter2 in enumerate(letter_list):
            if new_letter == letter2.key:
                returning_list.append(letter_list.pop(i))
                break

    return returning_list

def end_game_screen(operations, player_amount):
    """Function that prints out the scores when game ends"""
    print("These are the end scores: ")
    for i in range(player_amount):
        player = operations.get_next_turn()
        print(f"{player.name} ended the game with the score: {player.score}")

    print("Thanks for playing!\n")

if __name__ == "__main__":
    print("--Welcome to Scrabble!--")
    player_amount = 0
    operations = Operations() 
    pass_checker = 0
    player_lis = []

    while player_amount < 2 or player_amount > 4:
        player_amount = input("Choose how many are playing (2-4 players) or enter 1 to quit: ")

        try:
            player_amount = int(player_amount)
        except ValueError():
            print("You have to enter a number!")
            player_amount = 5
        
        if player_amount == 1:
            quit()
    
    
    pass_limit = 2 * player_amount #Set the pass limit for game end

    for i in range(1, player_amount + 1):
        player_input = input("Enter name for player {}: ".format(i))
        player_lis.append(player_input)
    
    operations.setup(player_lis) # Start the setup in operations class
    
    while pass_checker < pass_limit: # Game while loop, game ends when players have passed 2*player_amount times
        current_player = operations.get_next_turn() #Get current player class
        operations.print_board()
        print("\nPlayer {}, its your turn!\n".format(current_player.name))
        print("Current score: {}\n".format(current_player.display_score()))
        print("These are your letters:\n{}".format(current_player.display_letters()))

        option_input = ""

        while option_input != "1" and option_input != "2" and option_input != "3":
            print("These are your actions:\n1. Play letters\n2. Swap out letters\n3. Skip turn")
            option_input = input("Choose your action this turn: ")

    
            if option_input == "1": #If player chooses to play letters
                correct_pos = False
                while correct_pos == False: #Makes the player have to choose a valid position
                    row_input = int(input("Enter the row you wish to insert into: "))
                    column_input = int(input("Enter the column you wish to insert into: "))
                    correct_pos = operations.get_value_at_pos(row_input, column_input)
                    if correct_pos == False:
                        print("Invalid position")

                direction = ""
                while direction != "V" and direction != "H":
                    direction = input("Enter the direction (V for vertical and H for horizontal): ").capitalize()

                letter_list = choose_letters(current_player)
                if letter_list == None: # If player chooses to cancel we just reset the option input so the player can choose something else
                    option_input = ""
                else: # If player chooses to play letters we start the required operations
                    pass_checker = 0
                    total_letters_used = len(letter_list)
                    if correct_pos != "\u2605": # If the postion they chose is not the starting spot we add it before the order function
                        letter_list.append(correct_pos)

                    new_list = order_list(letter_list)
                    if correct_pos != "\u2605":
                        for i, letter in enumerate(new_list): #This changes the position input after where the player placed the letter that was already on the board
                            if letter.key == correct_pos.key:
                                if direction == "H":
                                    column_input = column_input - i
                                else:
                                    row_input = row_input - i
                                break

                    if operations.check_word(new_list): #Check if the word is valid and if so places it on the board
                        the_point = operations.play_letters(new_list, row_input, column_input, direction)
                        current_player.score += the_point
                        if operations.empty_check() == False: # If the bag is not empty draw more letters
                            operations.draw_letters(total_letters_used, current_player)
                    else:
                        if correct_pos != "\u2605": # Add the letters back on his hand but first remove the letter from the board if it was on hand
                            for i, letter in enumerate(new_list):
                                if letter.key == correct_pos.key:
                                    new_list.pop(i)
                                    break
                        operations.return_letters_to_hand(new_list, current_player)

            elif option_input == "2": # Asks you to choose which letters to swap if None allow a new action but if chosen then call the swap function in operations
                if operations.empty_check() == False: # Check if bag is empty
                    letter_list = choose_letters(current_player)
                    if letter_list == None:
                        option_input = ""
                    else:
                        pass_checker = 0
                        operations.swap_letters(letter_list, current_player)
                else:
                    print("Cannot swap when bag is empty")
            else: # Increase the pass_checker both the other options reset the checker
                pass_checker += 1
                continue

        if len(current_player.letter_list) == 0: # If player finishes letters and did not get new ones end the game
            break

    print("\nGame over")
    end_game_screen(operations, player_amount)









    