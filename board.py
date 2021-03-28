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