import api

# Get maze info
height = api.get_maze_height()
width = api.get_maze_width()
area = api.get_goal_area()
is_full_size = api.is_full_size()

# Search
api.front_wall_exists()
api.left_wall_exists()
api.right_wall_exists()

api.move_forward()

api.front_wall_exists()
api.left_wall_exists()
api.right_wall_exists()

api.turn_left()
api.move_forward()

api.front_wall_exists()
api.left_wall_exists()
api.right_wall_exists()

api.move_forward()

# for i in range(1024):
#     front = api.front_wall_exists()
# for i in range(1024):
#     left = api.left_wall_exists()
# for i in range(1024):
#     right = api.right_wall_exists()

# for i in range(10240//2):
#     api.move_forward(1)
#     api.turn_left()
#     api.turn_left()
# for i in range(640):
#     api.turn_left()
# for i in range(640):
#     api.turn_right()

# height = api.get_maze_height()
# width = api.get_maze_width()
# area = api.get_goal_area()
# is_full_size = api.is_full_size()

# for i in range(3072):
#     api.set_wall(1, 1, 0)
# api.clear_wall(1, 1, 0)

# for i in range(10240):
#     api.console_log('Hello')

# for i in range(10**7):
#     api.set_color(1, 1, 0)
# api.clear_color(1, 1)
# for i in range(10240):
#     api.clear_all_color()


# for i in range(10**7):
#     api.set_text(1, 1, '123')
# api.clear_text(1, 1)
# for i in range(10240):
#     api.clear_all_text()


api.save_history()
