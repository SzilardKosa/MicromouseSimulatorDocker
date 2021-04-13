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
