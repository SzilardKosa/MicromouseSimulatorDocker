import api


front = api.getFrontWall()
left = api.getLeftWall()
right = api.getRightWall()

api.moveForward()
api.turnLeft()
api.turnRight()

height = api.getMazeHeight()
width = api.getMazeWidth()
area = api.getGoalArea()
is_full_size = api.isFullSize()

api.setWall(1, 1, 0)
api.clearWall(1, 1, 0)

api.consoleLog('Hello')

api.setColor(1, 1, 0)
api.clearColor(1, 1)
api.clearAllColor()

api.setText(1, 1, 'Start')
api.clearText(1, 1)
api.clearAllText()
