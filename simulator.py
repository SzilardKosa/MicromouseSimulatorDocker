from maze import Maze
import subprocess
import sys
import time


class Simulator:
    def __init__(self):
        self.maze = Maze()

    def run(self):
        process = subprocess.Popen([sys.executable, r'shared/main.py'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, bufsize=0)

        while True:
            req = process.stdout.readline()
            print(req)
            if req == b'':
                break
            process.stdin.write(b'10\r\n')
        print('finished')
        print(process.returncode)


sim = Simulator()
sim.run()
