# вывести строки, содержащие двоичную запись числа, кратного 3
# решить без приведения строки к целому числу

'''
Input:
0
10010
00101
01001
Not a number
1 1
0 0

Output:
0
10010
01001
'''

import sys
import re


def update_state(num, state):
    # обновление состояния по пришедшему числу num
    if state == 0:
        if num == '1':
            state = 1
    elif state == 1:
        if num == '0':
            state = 2
        else:
            state = 0
    elif state == 2:
        if num == '0':
            state = 1
    return state

def div3(line):
    state = 0
    for elem in line:
        state = update_state(elem, state)
    return state


for line in sys.stdin:
    line = line.rstrip()
    pattern = r'[01]+'
    match = re.match(pattern, line)
    try:
        span = match.span()
        if span[1] == len(line):
            if div3(line) == 0:
                print(line)
    except AttributeError:
        pass

