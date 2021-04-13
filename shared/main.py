import api

front = api.get_front_wall()
left = api.get_left_wall()
right = api.get_right_wall()

api.move_forward(1)
api.turn_left()
api.turn_right()

height = api.get_maze_height()
width = api.get_maze_width()
area = api.get_goal_area()
is_full_size = api.is_full_size()

api.set_wall(1, 1, 0)
api.clear_wall(1, 1, 0)

api.console_log('Hello')

api.set_color(1, 1, 0)
api.clear_color(1, 1)
api.clear_all_color()

api.set_text(1, 1, '123')
api.clear_text(1, 1)
api.clear_all_text()
