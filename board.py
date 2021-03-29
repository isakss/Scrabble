class Board:
    def __init__(self, rows = 16, columns = 16):
        """Makes a board with * as empty spaces"""
        self.tile_char = "*"
        self.start_char = "\u2605"
        self.grid = []

        for i in range(rows):
            gridline = []
            for j in range(columns):
                if i == 0:
                    gridline.append(j)
                elif j == 0:
                    gridline.append(i)
                else:
                    gridline.append(self.tile_char)
            self.grid.append(gridline)
        
        self.insert_into_board(8, 8, self.start_char)
    
    def insert_into_board(self, row, column, value):
        self.grid[row][column] = value

    def get_value_at_pos(self, row, col):
        that_pos = self.grid[row][col]
        if that_pos == "*":
            return False
        else:
            return that_pos

    def add_word(self, letter_list, row, col, direction):
        """Takes in letters, position and direction and writes it out in that direction"""
        total_points = 0
        middle = self.get_value_at_pos(8,8)
        if (len(letter_list) == 7 and middle == "\u2605") or len(letter_list) == 8:
            total_points += 50

        for letter in letter_list:
            self.insert_into_board(row, col, letter)
            total_points += letter.points
            if direction == "V":
                row += 1
            else:
                col += 1

        return total_points

    def __str__(self):
        ret_str = ""

        for list_element in self.grid:
            for element in list_element:
                ret_str += " " + str(element) + " "
            ret_str += "\n"
        
        return ret_str