# https: // stackoverflow.com/questions/26464382/comunicate-between-2-processes-with-stdin-and-stdout
import subprocess
import sys

process = subprocess.Popen([sys.executable, r'B.py'], stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, bufsize=0)
for _ in range(30000):
    process.stdin.write(b'hello\n')
    process.stdout.readline()
