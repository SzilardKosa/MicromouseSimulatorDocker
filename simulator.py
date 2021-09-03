import json
import re
import shutil
import subprocess
import sys
import time

from maze import RIGHT, UP, Maze


class Simulator:
    def __init__(self):
        self.maze = Maze('shared/maze.json')
        self.mouse_state = {
            'x': 0,
            'y': 0,
            'dir': UP
        }
        self.routes = {
            # Sensor
            '^fw$': self.front_wall_exists,
            '^lw$': self.left_wall_exists,
            '^rw$': self.right_wall_exists,
            # Control
            '^mf [0-9]{1,2}$': self.move_forward,
            '^tl$': self.turn_left,
            '^tr$': self.turn_right,
            # Maze info
            '^mw$': self.get_maze_width,
            '^mh$': self.get_maze_height,
            '^ga$': self.get_goal_area,
            '^if$': self.is_full_size,
            # WRONG SYNTAX
            '.*': self.wrong_syntax
        }
        self.result = {
            'maze': self.maze.raw_json,
            'error': ''
        }

    def run(self):
        shutil.copy('shared/main.py', 'main.py')
        process = subprocess.Popen([sys.executable, r'main.py'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, bufsize=0)
        while True:
            req = process.stdout.readline()
            # print('Request: ', req)
            if req == b'':
                break
            res, err = self.handle_request(req.strip().decode('utf-8'))
            if err:
                self.result['error'] = err
                self.force_terminate(process)
                break
            # print('Response: ', res)
            process.stdin.write(f'{res}\r\n'.encode('utf-8'))
        print('FINISHED')
        self.save_result()

    def handle_request(self, req):
        for pattern, api_call in self.routes.items():
            if re.match(pattern, req):
                res, err = api_call(req)
                break
        return res, err

    def force_terminate(self, process):
        process.stdin.write(b'err\r\n')
        process.wait()

    def save_result(self):
        with open('shared/result.json', 'w') as result_file:
            json.dump(self.result, result_file)

    # API calls
    # Syntax error
    def wrong_syntax(self, req):
        err = f'Wrong syntax used: {req}'
        return None, err

    # Sensor
    def front_wall_exists(self, _=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = self.mouse_state['dir']
        res = self.maze.walls[x][y][direction]
        return res, None

    def left_wall_exists(self, _=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = (self.mouse_state['dir'] - 1) % 4
        res = self.maze.walls[x][y][direction]
        return res, None

    def right_wall_exists(self, _=None):
        x = self.mouse_state['x']
        y = self.mouse_state['y']
        direction = (self.mouse_state['dir'] + 1) % 4
        res = self.maze.walls[x][y][direction]
        return res, None

    # Control
    def move_forward(self, req):
        _, steps = req.split()
        err = None
        for _ in range(int(steps)):
            front_wall, _ = self.front_wall_exists()
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

    def turn_left(self, _):
        self.mouse_state['dir'] = (self.mouse_state['dir'] - 1) % 4
        return 'ok', None

    def turn_right(self, _):
        self.mouse_state['dir'] = (self.mouse_state['dir'] + 1) % 4
        return 'ok', None

    # Maze info
    def get_maze_width(self, _):
        res = self.maze.width
        return res, None

    def get_maze_height(self, _):
        res = self.maze.height
        return res, None

    def get_goal_area(self, _):
        p1_x = self.maze.goal_area['top_left']['x']
        p1_y = self.maze.goal_area['top_left']['y']
        p2_x = self.maze.goal_area['bottom_right']['x']
        p2_y = self.maze.goal_area['bottom_right']['y']
        res = [(p1_x, p1_y), (p2_x, p2_y)]
        return res, None

    def is_full_size(self, _):
        res = self.maze.is_full_size
        return res, None


t0 = time.time()
sim = Simulator()
sim.run()
t1 = time.time()
print("Run time: ", t1-t0)
