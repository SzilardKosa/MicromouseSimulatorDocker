import api

for i in range(1024):
    front = api.front_wall_exists()
for i in range(1024):
    left = api.left_wall_exists()
for i in range(1024):
    right = api.right_wall_exists()

for i in range(10240//2):
    api.move_forward(1)
    api.turn_left()
    api.turn_left()
for i in range(640):
    api.turn_left()
for i in range(640):
    api.turn_right()

height = api.get_maze_height()
width = api.get_maze_width()
area = api.get_goal_area()
is_full_size = api.is_full_size()

for i in range(10240):
    api.console_log('Hello')

for i in range(10**7):
    api.set_cell_text(1, 1, '123')

api.stop_simulation()
