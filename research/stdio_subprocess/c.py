# https: // stackoverflow.com/questions/26464382/comunicate-between-2-processes-with-stdin-and-stdout
import subprocess
import sys

process = subprocess.Popen([r'd.exe'], stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, bufsize=0)
for i in range(100000):
    process.stdin.write(b'10\n')
    res = process.stdout.readline()
    # if i % 10000 == 0:
    #     print(res)

# Checking reading terminated process
# process = subprocess.Popen([r'main.exe'], stdin=subprocess.PIPE,
#                            stdout=subprocess.PIPE, bufsize=0)
# for i in range(10):
#     # process.stdin.write(b'10\n')
#     res = process.stdout.readline()
#     print(res)
#     print(process.poll())
#     # if i % 10000 == 0:
#     #     print(res)
