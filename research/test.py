# string = '[(1,2),(1,2)]'

# print(eval(string))


# # regular expressions
# import re

# # exact match
# pattern = '^fw$'
# test_string = 'fw'
# print(re.match(pattern, test_string))

# # # match vs search
# # # https: // stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match

# # commmand with number arguments
# pattern = '^sw [0-9]{1,2} [0-9]{1,2} [0-3]$'
# test_string = 'sw 12 12 3'
# print(re.match(pattern, test_string))

# # commmand with string arguments
# pattern = '^cl '
# test_string = 'cl Hello World!'
# print(re.match(pattern, test_string))


# # switch test
# switch = {'one': 1, 'two': 2}
# print(switch.items())

# for k, i in switch.items():
#     print(i)
#     if i == 1:
#         break

# # test two param return
# def do_something(req):
#     return True, None


# res, err = do_something("Heyyo")

# print(res)
# print(err)

# import numpy as np

# a = np.array([['01', '11', '21'], ['00', '10', '20']])
# print(a)

# a = np.transpose(a)
# print(a)

# a = a[:, ::-1]
# print(a)


# Write to file

# file = open('test.txt', 'w')
import time

# # write chunk, without append
# t0 = time.time()
# with open('test.txt', 'w') as file:
#     chunk = 'hello\n'*2*10**7
#     file.write(chunk)
# t1 = time.time()
# print("Write 'hello\\n'*2*10**7: ", t1-t0)

# # write chunk, with append string
# t0 = time.time()
# with open('test.txt', 'w') as file:
#     chunk = []
#     for i in range(2*10**7):
#         chunk.append('hello\n')
#     file.write(''.join(chunk))
# t1 = time.time()
# print("Write using append: ", t1-t0)

# # write in loop
# t0 = time.time()
# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         file.write('hello\n')
# t1 = time.time()
# print("Write in loop: ", t1-t0)

# # writelines without append
# t0 = time.time()
# with open('test.txt', 'w') as file:
#     chunk = ['hello\n']*2*10**7
#     file.writelines(chunk)
# t1 = time.time()
# print("Writelines ['hello\\n']*2*10**7: ", t1-t0)

# # writelines append
# t0 = time.time()
# with open('test.txt', 'w') as file:
#     chunk = []
#     for i in range(2*10**7):
#         chunk.append('hello\n')
#     file.writelines(chunk)
# t1 = time.time()
# print("Writelines using append: ", t1-t0)

# # write using global var and a function
# t0 = time.time()
# chunk = []

# def push(item):
#     global chunk
#     chunk.append(item)

# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         push('hello\n')
#     file.write(''.join(chunk))
#     # file.writelines(chunk)
# t1 = time.time()
# print("Write using append, and global var: ", t1-t0)


# # Adding string format
# t0 = time.time()
# chunk = []
# def push(item):
#     global chunk
#     chunk.append(item)
# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         a = 1
#         b = 3
#         push(f'hello {a} {b}\n')
#     file.write(''.join(chunk))
# t1 = time.time()
# print("f'' formating ", t1-t0)

# # Adding string format
# t0 = time.time()
# chunk = []
# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         a = 1
#         b = 3
#         push('hello '+str(a)+' '+str(b)+' \n')
#     file.write(''.join(chunk))
# t1 = time.time()
# print("+' '+ formating ", t1-t0)

# # Adding percent format
# t0 = time.time()
# chunk = []
# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         a = 1
#         b = 3
#         push('hello %s %s \n' % (a, b))
#     file.write(''.join(chunk))
# t1 = time.time()
# print("pct formating ", t1-t0)

# # Join format
# t0 = time.time()
# chunk = []
# with open('test.txt', 'w') as file:
#     for i in range(2*10**7):
#         a = 1
#         b = 3
#         push('hello')
#         push(str(a))
#         push(str(b))
#         push('\n')
#     file.write(''.join(chunk))
# t1 = time.time()
# print("join formating ", t1-t0)



# import shutil

# shutil.copy('shared/copyme.py', 'copyme.py')


# matrix = [
#   [[True, False],[True, False],[True, False]],
#   [[True, False],[True, False],[True, False]]
# ]
# print(matrix)
# print()
# print(*matrix)
# print()
# print([*zip(*matrix)])

# # https://stackoverflow.com/questions/4937491/matrix-transpose-in-python
# # https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139418
# tmatrix = [*zip(*matrix)]

matrix = [([0,1],[2,3]), ([4,5],[6,7])]

print([m[::-1] for m in matrix])