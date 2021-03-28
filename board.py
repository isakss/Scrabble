class Board:
    def __init__(self, rows = 15, columns = 15):
        self.tile_char = "*"
        self.start_char = "\u2605"
        self.grid = []

        for i in range(rows):
            gridline = []
            for j in range(columns):
                gridline.append(self.tile_char)
            self.grid.append(gridline)
        
        self.insert_into_board(7, 7, self.start_char)
    
    def insert_into_board(self, x, y, value):
        self.grid[x][y] = value

    def get_value_at_pos(self, row, col):
        that_pos = self.grid[row][col]
        if that_pos == "*":
            return False
        else:
            return that_pos

    def add_word(self, letter_list, row, col, direction):
        total_points = 0
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

if __name__ == "__main__":
    new_board = Board()

    print(new_board)

    new_board.insert_into_board(7, 7, "A")

    print(new_board)

    new_board.insert_into_board(4,7,"B")

    print(new_board)