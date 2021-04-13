import sys


def request(args):
    msg = ' '.join([str(x) for x in args])
    print(msg)
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    return response


# Sensor
def get_front_wall():
    return request(['fw']) == 'True'  # str to boolean


def get_left_wall():
    return request(['lw']) == 'True'


def get_right_wall():
    return request(['rw']) == 'True'


# Control
def move_forward(steps=1):
    request(['mf', steps])


def turn_left():
    request(['tl'])


def turn_right():
    request(['tr'])


# Maze info
def get_maze_width():
    return int(request(['mw']))


def get_maze_height():
    return int(request(['mh']))


def get_goal_area():
    # https://www.geeksforgeeks.org/python-convert-string-to-tuple-list/
    return eval(request(['ga']))


def is_full_size():
    return request(['if']) == 'True'


# Feedback: Wall
def set_wall(x, y, direction):
    request(['sw', x, y, direction])


def clear_wall(x, y, direction):
    request(['cw', x, y, direction])


# Feedback: Console
def console_log(text):
    request(['cl', text])


# Feedback: Cell color
def set_color(x, y, color):
    request(['sc', x, y, color])


def clear_color(x, y):
    request(['cc', x, y])


def clear_all_color():
    request(['cac'])


# Feedback: Cell text
def set_text(x, y, text):
    request(['st', x, y, text])


def clear_text(x, y):
    request(['ct', x, y])


def clear_all_text():
    request(['cat'])
