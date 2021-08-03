import sys

history = []

def request(args):
    msg = ' '.join([str(x) for x in args])
    print(msg)
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    if response == 'err':
        force_shutdown()
    return response

def push_to_history(cmd):
    global history
    history.append(cmd)

def force_shutdown():
    save_history()
    sys.exit(1)

def save_history():
    with open('shared/history.txt', 'w') as file:
        file.write(''.join(history))


# Sensor
def front_wall_exists():
    push_to_history('fw\n')
    return request(['fw']) == 'True'  # str to boolean


def left_wall_exists():
    push_to_history('lw\n')
    return request(['lw']) == 'True'


def right_wall_exists():
    push_to_history('rw\n')
    return request(['rw']) == 'True'


# Control
def move_forward(steps=1):
    push_to_history(f'mf {steps}\n')
    request(['mf', steps])


def turn_left():
    push_to_history('tl\n')
    request(['tl'])


def turn_right():
    push_to_history('tr\n')
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
    push_to_history(f'sw {x} {y} {direction}\n')


def clear_wall(x, y, direction):
    push_to_history(f'cw {x} {y} {direction}\n')


# Feedback: Console
def console_log(text):
    push_to_history(f'cl {text}\n')


# Feedback: Cell color
def set_color(x, y, color):
    push_to_history(f'sc {x} {y} {color}\n')


def clear_color(x, y):
    push_to_history(f'cc {x} {y}\n')


def clear_all_color():
    push_to_history('cac\n')


# Feedback: Cell text
def set_text(x, y, text):
    push_to_history(f'st {x} {y} {text}\n')


def clear_text(x, y):
    push_to_history(f'ct {x} {y}\n') 


def clear_all_text():
    push_to_history('cat\n')
