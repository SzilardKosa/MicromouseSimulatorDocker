import json
import re
import subprocess
import sys
import time

from maze import DOWN, LEFT, RIGHT, UP, Maze


class Simulator:
    def __init__(self):
        self.maze = Maze()
        self.mouse_state = {
            'x': 0,
            'y': 0,
            'dir': UP
        }
        self.routes = {
            # Sensor
            '^fw$': self.get_front_wall,
            '^lw$': self.get_left_wall,
            '^rw$': self.get_right_wall,
            # Control
            '^mf [0-9]{1,2}$': self.move_forward,
            '^tl$': self.turn_left,
            '^tr$': self.turn_right,
            # Maze info
            '^mw$': self.get_maze_width,
            '^mh$': self.get_maze_height,
            '^ga$': self.get_goal_area,
            '^if$': self.is_full_size,
            # Feedback: Wall
            '^sw [0-9]{1,2} [0-9]{1,2} [0-3]$': self.save_with_position_check,
            '^cw [0-9]{1,2} [0-9]{1,2} [0-3]$': self.save_with_position_check,
            # Feedback: Console
            '^cl ': self.save_without_check,
            # Feedback: Cell color
            '^sc [0-9]{1,2} [0-9]{1,2} [0-9]$': self.save_with_position_check,
            '^cc [0-9]{1,2} [0-9]{1,2}$': self.save_with_position_check,
            '^cac$': self.save_without_check,
            # Feedback: Cell text
            '^st [0-9]{1,2} [0-9]{1,2} .{1,4}$': self.save_with_position_check,
            '^ct [0-9]{1,2} [0-9]{1,2}$': self.save_with_position_check,
            '^cat$': self.save_without_check,
            # WRONG SYNTAX
            '.*': self.wrong_syntax
        }
        self.result = {
            'maze': self.maze.raw_json,
            'commands': [],
            'error': ''
        }

    def run(self):
        process = subprocess.Popen([sys.executable, r'shared/main.py'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, bufsize=0)
        while True:
            req = process.stdout.readline()
            print('Request: ', req)
            if req == b'':
                break
            res, err = self.handle_request(req.strip().decode('utf-8'))
            if err:
                self.result['error'] = err
                process.terminate()
                break
            print('Response: ', res)
            process.stdin.write(f'{res}\r\n'.encode('utf-8'))
        print('FINISHED')
        self.save_result()

    def handle_request(self, req):
        for pattern, api_call in self.routes.items():
            if re.match(pattern, req):
                res, err = api_call(req)
                break
        return res, err

    def save_result(self):
        with open('shared/result.json', 'w') as result_file:
            json.dump(self.result, result_file)

    # API calls
    # Syntax error
    def wrong_syntax(self, req):
        err = f'Wrong syntax used: {req}'
        return None, err

    # Sensor
    def get_front_wall(self, req=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = self.mouse_state['dir']
        res = self.maze.walls[x, y, direction]
        return res, None

    def get_left_wall(self, req=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = (self.mouse_state['dir'] - 1) % 4
        res = self.maze.walls[x, y, direction]
        return res, None

    def get_right_wall(self, req=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = (self.mouse_state['dir'] + 1) % 4
        res = self.maze.walls[x, y, direction]
        return res, None

    # Control
    def move_forward(self, req):
        cmd, steps = req.split()
        err = None
        for _ in range(int(steps)):
            self.result['commands'].append(cmd)
            front_wall, _ = self.get_front_wall()
            # if we go into a wall
            if front_wall:
                err = 'The mouse cannot move through the walls!'
                break
            else:
                self.move_one()
        return 'ok', err

    def move_one(self):
        direction = self.mouse_state['dir']
        if direction % 2 == 0:  # UP = 0, DOWN = 2
            self.mouse_state['y'] += 1 if direction == UP else - 1
        else:  # RIGHT = 1, LEFT = 3
            self.mouse_state['x'] += 1 if direction == RIGHT else - 1

    def turn_left(self, req):
        self.result['commands'].append(req)
        self.mouse_state['dir'] = (self.mouse_state['dir'] - 1) % 4
        return 'ok', None

    def turn_right(self, req):
        self.result['commands'].append(req)
        self.mouse_state['dir'] = (self.mouse_state['dir'] + 1) % 4
        return 'ok', None

    # Maze info
    def get_maze_width(self, req):
        res = self.maze.width
        return res, None

    def get_maze_height(self, req):
        res = self.maze.height
        return res, None

    def get_goal_area(self, req):
        p1_x = self.maze.goal_area['top_left']['x']
        p1_y = self.maze.goal_area['top_left']['y']
        p2_x = self.maze.goal_area['bottom_right']['x']
        p2_y = self.maze.goal_area['bottom_right']['y']
        res = [(p1_x, p1_y), (p2_x, p2_y)]
        return res, None

    def is_full_size(self, req):
        res = self.maze.is_full_size
        return res, None

    # Feedback: Wall, Console, Color, Text
    def save_with_position_check(self, req):
        self.result['commands'].append(req)
        x, y = req.split()[1:3]
        err = self.check_position(int(x), int(y))
        return 'ok', err

    def check_position(self, x, y):
        err = None
        if x > (self.maze.width - 1):
            err = 'The \'x\' parameter is outside of the maze!'
        if y > (self.maze.height - 1):
            err = 'The \'y\' parameter is outside of the maze!'
        return err

    def save_without_check(self, req):
        self.result['commands'].append(req)
        return 'ok', None


sim = Simulator()
sim.run()
