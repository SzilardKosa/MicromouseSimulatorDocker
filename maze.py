import json


class Maze:
    def __init__(self):
        self.load_maze('shared/maze.json')
        self.parse_maze_map()

    def load_maze(self, path):
        with open(path) as maze_file:
            raw_maze = json.load(maze_file)
        self.width = raw_maze['width']
        self.height = raw_maze['height']
        self.is_full_size = raw_maze['is_full_size']
        self.raw_map = raw_maze['maze_map']

    def parse_maze_map(self):
        self.walls = [[{'top': False, 'left': False, 'bottom': False, 'right': False}
                       for col in range(self.width)]
                      for row in range(self.height)]
        row_width = 4 * self.width + 2
        cell_width = 4
        for row in range(self.height):
            for col in range(self.width):
                x_offset = col * cell_width
                y_offset = row * row_width * 2
                cell_offset = x_offset + y_offset  # offset to cell data in raw_map string
                top_position = cell_width // 2 + cell_offset
                left_position = row_width + cell_offset
                bottom_position = 2 * row_width + cell_width // 2 + cell_offset
                right_position = row_width + cell_width + cell_offset
                self.walls[row][col]['top'] = self.raw_map[top_position] == '-'
                self.walls[row][col]['left'] = self.raw_map[left_position] == '|'
                self.walls[row][col]['bottom'] = self.raw_map[bottom_position] == '-'
                self.walls[row][col]['right'] = self.raw_map[right_position] == '|'


maze = Maze()
# print(maze.raw_map)
