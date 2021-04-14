import json

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Maze:
    def __init__(self):
        self.load_maze('shared/maze.json')
        self.parse_maze_map()

    def load_maze(self, path):
        with open(path) as maze_file:
            self.raw_json = json.load(maze_file)
        self.width = self.raw_json['width']
        self.height = self.raw_json['height']
        self.is_full_size = self.raw_json['is_full_size']
        self.goal_area = self.raw_json['goal_area']
        self.raw_map = self.raw_json['maze_map']

    def parse_maze_map(self):
        self.walls = [[[False, False, False, False]
                       for col in range(self.width)]
                      for row in range(self.height)]
        row_width = 4 * self.width + 2
        cell_width = 4
        for row in range(self.height):
            for col in range(self.width):
                # Offset in the string
                x_offset = col * cell_width
                y_offset = row * row_width * 2
                # Summing the offsets
                cell_offset = x_offset + y_offset
                # Calculating wall position in the raw_map string
                top_position = cell_width // 2 + cell_offset
                right_position = row_width + cell_width + cell_offset
                bottom_position = 2 * row_width + cell_width // 2 + cell_offset
                left_position = row_width + cell_offset
                # Storing the wall states for the current cell
                self.walls[row][col][UP] = self.raw_map[top_position] == '-'
                self.walls[row][col][RIGHT] = self.raw_map[right_position] == '|'
                self.walls[row][col][DOWN] = self.raw_map[bottom_position] == '-'
                self.walls[row][col][LEFT] = self.raw_map[left_position] == '|'
        # transpose (1,0,2)
        # [row][col] => [col][row]
        # [yn - y0][x0 - xn] => [x0 - xn][yn - y0]
        self.walls =  [*zip(*self.walls)]
        # reverse row indexes
        # [x0 - xn][yn - y0] => [x0 - xn][y0 - yn]
        self.walls = [m[::-1] for m in self.walls]


# maze = Maze()

# # Testing cell (0,0)
# assert maze.walls[0][0][UP] == False
# assert maze.walls[0][0][RIGHT] == True
# assert maze.walls[0][0][DOWN] == True
# assert maze.walls[0][0][LEFT] == True

# # Testing cell (1,0)
# assert maze.walls[1][0][UP] == True
# assert maze.walls[1][0][RIGHT] == False
# assert maze.walls[1][0][DOWN] == True
# assert maze.walls[1][0][LEFT] == True
