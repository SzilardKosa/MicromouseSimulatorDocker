import sys


def request(args):
    msg = ' '.join([str(x) for x in args])
    print(msg)
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    return response


# Sensor
def getFrontWall():
    return request(['fw']) == 'True'  # str to boolean


def getLeftWall():
    return request(['lw']) == 'True'


def getRightWall():
    return request(['rw']) == 'True'


# Control
def moveForward(steps=1):
    request(['mf', steps])


def turnLeft():
    request(['tl'])


def turnRight():
    request(['tr'])


# Maze info
def getMazeWidth():
    return int(request(['mw']))


def getMazeHeight():
    return int(request(['mh']))


def getGoalArea():
    # https://www.geeksforgeeks.org/python-convert-string-to-tuple-list/
    return eval(request(['ga']))


def isFullSize():
    return request(['if']) == 'True'


# Feedback: Wall
def setWall(x, y, direction):
    request(['sw', x, y, direction])


def clearWall(x, y, direction):
    request(['cw', x, y, direction])


# Feedback: Console
def consoleLog(text):
    request(['cl', text])


# Feedback: Cell color
def setColor(x, y, color):
    request(['sc', x, y, color])


def clearColor(x, y):
    request(['cc', x, y])


def clearAllColor():
    request(['cac'])


# Feedback: Cell text
def setText(x, y, text):
    request(['st', x, y, text])


def clearText(x, y):
    request(['ct', x, y])


def clearAllText():
    request(['cat'])
