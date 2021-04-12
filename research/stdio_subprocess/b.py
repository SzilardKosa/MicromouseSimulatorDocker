import sys

for line in sys.stdin:
    print('Send back', line.strip())
    sys.stdout.flush()
