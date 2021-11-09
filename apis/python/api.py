import sys

history = []
MSG_START = '$'


def request(args):
    msg = MSG_START + ' '.join([str(x) for x in args])
    print(msg)
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    if response == 'end':
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
    response = request(['ga'])
    values = response.split()
    goal_area = {
        "top_left":
        {
            "x": values[0],
            "y": values[1]
        },
        "bottom_right":
        {
            "x": values[2],
            "y": values[3]
        }
    },
    return goal_area


def is_full_size():
    return request(['if']) == 'True'


# Feedback: Console
def console_log(text):
    push_to_history(f'cl {text}\n')


# Feedback: Cell text
def set_cell_text(x, y, text):
    push_to_history(f'st {x} {y} {text}\n')


# Stop simulation
def stop_simulation():
    request(['ss'])
